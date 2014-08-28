import logging
import re
import xmlformatter
import xml.etree.ElementTree as ET
from mfw.dataprovider import utils


class BscHwConfUpdater(object):

    def __init__(self, info_source=None):

        self.logger = logging.getLogger(__name__)

        self.masterfile = info_source
        self.filelist = utils.get_all_files(info_source)
        self.full_dt = utils.get_all_dt(self.filelist)
        self.full_dict = utils.AxeParser(self.full_dt)

        try:
            self.saefile = re.findall('/.*SAE.*/(.+)', self.filelist)[0]
        except:
            self.logger.error('SAE file not found in masterfile')
            exit()
        self.tssfiles = re.findall('/.*TSS.*/(.+)', self.filelist)

        nodeinfo_data = self.read_nodeinfo_data_new()
        ip_data = read_ip_data(self.full_dict, ('RTIPGSH',
                                                'RTIPCTH',
                                                'RTIPGPH',
                                                'RTIPPGW',
                                                'RTIPAGW'))
        self.rp_data = read_rp_data(self.full_dict)
        self.dtset_data = read_dtset_data(self.tssfiles)
        self.gbip_data = read_gbip_data(self.full_dict)
        self.piu_data = read_piu_data(self.full_dict)
        self.sigtran_own_data = read_c7_sigtran_own_data(self.full_dict)
        self.sigtran_node_data = read_c7_sigtran_node_data(self.full_dict)

        try:
            o_root = ET.Element("root")

            o_system = ET.SubElement(o_root, 'system')
            ET.SubElement(o_system, 'nodeinfo', nodeinfo_data)

            o_ip_data = ET.SubElement(o_root, 'ip_data')

            for i in ip_data:
                ET.SubElement(o_ip_data, 'ip', i)

            o_rp_data = ET.SubElement(o_root, 'rp_data')

            for i in self.rp_data:
                ET.SubElement(o_rp_data, 'rp', i)

            o_dtset_list = ET.SubElement(o_root, 'dtset_list')

            for i in self.dtset_data:
                ET.SubElement(o_dtset_list, 'dtset', i)

            o_gbip = ET.SubElement(o_root, 'gbip')

            for i in self.gbip_data:
                ET.SubElement(o_gbip, 'nsei', i)

            o_piu = ET.SubElement(o_root, 'piu_list')

            for i in self.piu_data:
                ET.SubElement(o_piu, 'piu', i)

            o_c7ip = ET.SubElement(o_root, 'c7ip')
            ET.SubElement(o_c7ip, 'own_data', self.sigtran_own_data[0])

            for i in self.sigtran_node_data:
                ET.SubElement(o_c7ip, 'node', i)
        except:
            logging.warning("Some data has not been extracted from DT")

        self.xmlstring = xmlformatter.Formatter().format_string(ET.tostring(o_root)).decode()  # noqa

    def read_nodeinfo_data(self):

        nodeinfo = {}

        m_o = re.search('master_dt_file_(BSC\d+)', self.masterfile)

        nodeinfo['name'] = m_o.group(1)

        m_o = re.search('SAE_([^_]+)_([^_]+)_([^_]+)_([^_]+)_([^_]+)_(\w+)',
                        self.saefile)

        nodeinfo['transmission'] = m_o.group(1).lower()
        nodeinfo['nodetype'] = m_o.group(2)
        nodeinfo['type'] = m_o.group(3)
        nodeinfo['apz'] = m_o.group(4)
        nodeinfo['apzvariant'] = m_o.group(5)
        nodeinfo['sigvariant'] = m_o.group(6)
        nodeinfo['btsbox'] = '0'
        nodeinfo['realcells'] = '0'

        return nodeinfo

    def read_nodeinfo_data_new(self):

        def add_(s):
            return "_" + s + "_"

        def add_dot(s):
            return "_" + s + "."

        nodeinfo = {}
        # acceptable element values
        nodetype = ["BEAMON", "CLASSIC", "CLASSIC_NNRP5", "EVO8200"]
        apz = ["21233", "21255", "21260"]
        apzvariant = ["2G", "4G", "4G_1C4T",
                      "E4", "E8", "E16", "S4", "S8", "S16"]
        trtype = ["BSC", "BSCTRC", "TRC"]
        transmission = ["CME20", "CMS40"]
        sigvariant = ["SIGTRAN_TO_MSC"]

        # make sure that both lists are updated in the same time
        data = [nodetype, apz, apzvariant, trtype, transmission, sigvariant]
        key_names = ['nodetype', 'apz', 'apzvariant',
                     'type', 'transmission', 'sigvariant']

        m_o = re.search('master_dt_file_(BSC\d+)', self.masterfile)
        nodeinfo['name'] = m_o.group(1)

        nodeinfo['btsbox'] = '0'
        nodeinfo['realcells'] = '0'

        s = self.saefile.upper()

        for index in range(len(key_names)):
            nodeinfo[key_names[index]] = 'undefined'
            for i in data[index]:
                tmp = s.find(add_(i)) + s.find(add_dot(i)) + 1
                if tmp >= 0:
                    nodeinfo[key_names[index]] = self.saefile[tmp + 1: tmp + 1 + len(i)]  # noqa
                    # element value is saved directly from original file name
                    break
        return nodeinfo


def read_ip_data(dt, ipdevtypes):

    ip_application_l = []

    rripi = utils.FindCommand(dt, 'RRIPI')
    rrapi = utils.FindCommand(dt, 'RRAPI')

    for i in rripi:
        if i['IPDEVTYPE'] in ipdevtypes:
            ip_ip_application_d = {}
            if i['IPADDR'][:7] != '192.168':
                ip_ip_application_d['ipdevtype'] = i['IPDEVTYPE']
                ip_ip_application_d['addr'] = i['IPADDR']
                ip_ip_application_d['netmask'] = i['MASK']
                try:
                    ip_ip_application_d['ipdevno'] = i['IPDEVNO']
                except:
                    pass
                apl = []
                for j in rrapi:
                    if j['IPADDR'] == i['IPADDR']:
                            apl.append(j['APL'])
                ip_ip_application_d['apl'] = ",".join(set(apl))
                ip_application_l.append(ip_ip_application_d)

    return ip_application_l


def read_rp_data(dt):

    rp_l = []
    rp_t = []
    rp_eqm_l = []
    rp_eqm_d = {}

    app_map = {'RTIPCTH': 'CTH',
               'RTIPGPH': 'GPH',
               'RTIPGSH': 'GSH',
               'ETM4': 'EVOET',
               'RTIPTRH': 'TRH',
               'RTIPAGW': 'AGW',
               'RTIPPGW': 'PGW',
               'XM': 'GS890XM',
               'CLM': 'GS890CLM',
               'RTTG1S': 'TRA7',
               'SCTP': 'SIGTRAN',
               'ETM2': 'ET1551E',
               'ETM3': 'ET1551A',
               'MUX34': 'GS890MUX',
               'C7STH': 'SS7ERRP'}

    tmp_l = utils.FindParam(dt, {'name': 'EXRPI', 'RP': '*', 'TYPE': '*'})

    for i in tmp_l:
        rp_t.append([i['RP'], i['TYPE']])

    tmp_l = utils.FindParam(dt, {'name': 'EXEMI', 'RP': '*', 'EQM': '*'})

    for i in tmp_l:
        rp_eqm_l.append([i['RP'], i['EQM']])

    for rp in rp_eqm_l:
        try:
            rp_eqm_d[rp[0]].append(rp[1].split('-')[0])
        except KeyError:
            rp_eqm_d[rp[0]] = [rp[1].split('-')[0], ]

    for rp in rp_t:
        rp_d = {}
        rp_d['number'] = rp[0]
        rp_d['type'] = rp[1]

        m_o = utils.FindParam(dt, {'name':
                                   'DBTSI', 'TAB':
                                   'RPSRPIRPS', 'RPADDR': rp[0]})

        if m_o:
            rp_d['ethgroup'] = m_o[0]['GROUP']

        m_o = utils.FindParam(dt, {'name': 'DBTSI', 'TAB': 'RPSARDRPS',
                                   'RPADDR': rp[0], 'GRPID': '*'})

        if m_o:
            rp_d['grpid'] = m_o[0]['GRPID']

        m_o = utils.FindParam(dt, {'name': 'DBTSI',
                                   'TAB': 'RPSRPBSPOS',
                                   'RPADDR': rp[0],
                                   'BRNO': '*',
                                   'MAGNO': '*',
                                   'SLOTNO': '*',
                                   'BUSCONN': '*'})

        if m_o:
            rp_d['brno'] = m_o[0]['BRNO']
            rp_d['magno'] = m_o[0]['MAGNO']
            rp_d['slotno'] = m_o[0]['SLOTNO']
            rp_d['busconn'] = m_o[0]['BUSCONN']

        m_o = utils.FindParam(dt, {'name': 'DBTSI',
                                   'TAB': 'RPSRPBSPOS',
                                   'RPADDR': rp[0],
                                   'BRNO': '*',
                                   'MAGNO': '*',
                                   'SLOTNO': '*',
                                   'INDNO': '*',
                                   'BUSCONN': '*'})

        if m_o:
            rp_d['brno'] = m_o[0]['BRNO']
            rp_d['magno'] = m_o[0]['MAGNO']
            rp_d['slotno'] = m_o[0]['SLOTNO']
            rp_d['indno'] = m_o[0]['INDNO']
            rp_d['busconn'] = m_o[0]['BUSCONN']

        for k, v in app_map.items():

            try:
                if k in rp_eqm_d[rp[0]]:
                    rp_d['application'] = v
            except KeyError:
                rp_d['application'] = 'UNKNOWN'
        rp_l.append(rp_d)
    return rp_l


def read_dtset_data(tssfiles):
    dtset_l = []
    for f in tssfiles:
        dtset_d = {}
        m_o = re.search('(TSS\d+)_([^\.]+)', f)
        if m_o:
            dtset_d['tss'] = m_o.group(1)
            dtset_d['type'] = m_o.group(2)
            dtset_l.append(dtset_d)
    return dtset_l


def read_gbip_data(dt):

    nsei_l = []

    t_l = utils.FindParam(dt, {'name': 'RRINI', 'NSEI': '*', 'PRIP': '*'})

    for i in t_l:
        t_d = {}
        t_d['nsei'] = i['NSEI']
        t_d['prip'] = i['PRIP']
        nsei_l.append(t_d)

    return nsei_l


def read_piu_data(dt):
    piu_l = []

    t_l = utils.FindParam(dt, {'name': 'DBTSI', 'TAB': 'RPSARDPIUS',
                               'MAGNO': '*', 'SLOTNO': '*',
                               'BOARD': '*', 'CONFNO': '*'})

    for i in t_l:
        t_d = {}

        t_d['magno'] = i['MAGNO']
        t_d['slotno'] = i['SLOTNO']
        t_d['board'] = i['BOARD']
        t_d['confno'] = i['CONFNO']
        piu_l.append(t_d)
    return piu_l


def read_c7_sigtran_own_data(_dict):

    own_l = []
    t_d = {}

    m_o = utils.FindParam(_dict, {'name': 'IHIFC', 'VIF': 'ETHA', 'IP': '*'})
    if m_o:
        t_d['ipa'] = m_o['IP']

    m_o = utils.FindParam(_dict, {'name': 'IHIFC', 'VIF': 'ETHB', 'IP': '*'})
    if m_o:
        t_d['ipa'] = m_o['IP']

    m_o = utils.FindParam(_dict, {'name': 'IHRSI', 'GW': '*',
                                  'PINGA': '*', 'PINGB': '*'})

    if m_o:
        m_o = m_o[0]
        t_d['gwa'] = m_o['GW'][:m_o['GW'].find("&")]
        t_d['gwb'] = m_o['GW'][m_o['GW'].find("&") + 1:]
        t_d['pinga'] = m_o['PINGA']
        t_d['pingb'] = m_o['PINGB']

    own_l.append(t_d)

    return own_l


def read_c7_sigtran_node_data(_dict):

    node_l = []

    # find signalling points

    sp_l = utils.FindParam(_dict, {'name': 'C7SPI', 'SP': '*'})

    for sp in sp_l:
        t_d = {}
        t_d = get_data_for_sp(sp['SP'], _dict)
        node_l.append(t_d)

    return node_l


def get_data_for_sp(sp, _dict):

    ssn_map = {'254': 'msc', '252': 'smlc'}
    t_d = {}

    t_d['sp'] = sp

    m_o = utils.FindParam(_dict, {'name': 'C7NSI', 'SP': sp, 'SSN': '*'})

    if m_o:
        try:
            ssn = m_o[0]['SSN']
            t_d['ssn'] = ssn
            t_d['type'] = ssn_map[ssn]
        except KeyError:
            logging.warning('Unknown node type, SSN=%s' % ssn)
            return None
    else:
        # not found SSN for SP which probably means
        # that this is MGW

        t_d['type'] = 'mgw'

        return t_d

    if t_d['type'] == 'msc':

        # find MSC name
        m_o = utils.FindParam(_dict, {'name': 'RRMBI', 'MSC': '*', 'SP': sp})

        if m_o:
            t_d['msc'] = m_o[0]['MSC']
    else:
        # search for DPC and NEI
        # for now we don't know if these must match the SP parts
        # but we'll fake it anyway

        m_o = re.search('(\d+)-(\d+)', sp)

        if m_o:
            t_d['nei'] = m_o.group(1)
            t_d['dpc'] = m_o.group(2)

    m_o = utils.FindParam(_dict, {'name': 'C7PNC', 'SPID': '*', 'SP': sp})

    if m_o:
        t_d['spid'] = m_o[0]['SPID']

    m_o = utils.FindParam(_dict, {'name': 'M3RSI', 'SAID': '*', 'DEST': sp})

    if m_o:
        t_d['said'] = m_o[0]['SAID']
    else:
        # need to dig this, possibly old sigtran here
        logging.warning('Command M3RSI not found, SIGTRAN data not available')
        return t_d

    m_o = utils.FindParam(_dict, {'name': 'IHADI', 'SAID': t_d['said'],
                                  'EPID': '*', 'RIP': '*', 'RPN': '*'})

    if m_o:
        t_d['epid'] = m_o[0]['EPID']
        t_d['rip'] = m_o[0]['RIP'].split('&')[0].replace('"', '')
        t_d['rpn'] = m_o[0]['RPN']

    m_o = utils.FindParam(_dict, {'name': 'IHBII',
                                  'EPID': t_d['epid'], 'LPN': '*'})

    if m_o:
        t_d['lpn'] = m_o[0]['LPN']

    return t_d
        