from mfw.dataprovider import DataProvider
import xml.etree.ElementTree as ET
from mfw.dataprovider import bschwcc


class HwData(DataProvider):

    def __init__(self, file):
        super().__init__()
        self.data = {}
        # wybrac lepsza wersje
        self.data['source'] = self.find_data_type(file)
        self.source = self.find_data_type(file)
        self.generate(file)

        
    def find_data_type(self , file):
        '''
        Check which type of data is provided in the file and return it.
        '''
        if '\\' in file:
            name = file[file.rfind('\\')+1:]
        if '/' in file:
            name = file[file.rfind('/')+1:]
        print (name)
        if name[-3:].lower() == 'xml': 
            return 'XML'
        elif name[:14] == 'master_dt_file':
            return 'MF' 
        else:
            return 'UNKNOWN TYPE'
        
    def generate(self,file):
        # Do some stuff
        self.logger.debug('Hw data controller is executed!')
        data_type=self.data['source']
        if data_type == 'XML':
            self.parse_XML(file)
        elif data_type == 'MF':
            self.parse_MF(file)
        elif data_type == 'UNKNOWN TYPE':
            pass
        else:
            self.logger.error('Incorrect data type.')

        print('Hw data controller is executed!')
        print(data_type)
        
        return "HW_DATA_STRUCTURE"

    def execute(self):
        return self.data

    def parse_XML(self,file):
        try:
            tree = ET.parse(file)
            self.logger.info('HW XML file %s processed successfuly' % file)
        except ET.ParseError as err:
            self.logger.error(err)
            return
        root = tree.getroot()

        keys = {'nodeinfo':['system','nodeinfo'],
                 'piu_list':['piu_list','piu'],
                 'rp_data':['rp_data','rp'],
                 'ip_data':['ip_data', 'ip'],
                 'gbip':['gbip', 'nsei'],
                 'sigtran_own':['c7ip', 'own_data'],
                 'sigtran_nodes':['c7ip', 'node'],
                 'dtset_list':['dtset_list', 'dtset']
                 }
        for i in keys.keys():
            self.data[i]=self.parse_xml(root, keys[i][0], keys[i][1])

        print(self.get('rp_data'))
        print(self.get('rp_dat'))

    def parse_MF(self,file):
        hw_data = bschwcc.BscHwConfUpdater(file)
        self.data['nodeinfo'] = [hw_data.read_nodeinfo_data_new()]
        self.data['filelist'] = self.filelist_transform(hw_data.filelist)
        self.data['rp_list'] = hw_data.rp_data
        self.data['dtset_list'] = hw_data.dtset_data        

    def get(self,key):
        if key in self.data.keys():
            return self.data[key]
        else:
            self.logger.error('Missing key: %s' % key)
            

    def parse_xml(self, root, parent_string, iter_string):

        et = root.find(parent_string)
        if et is not None:
            common = et.attrib
            t_list = []

            for i in et.iter(iter_string):
                t_dict = common.copy()
                t_dict.update(i.attrib)
                t_list.append(t_dict)
            return t_list
        else:
            self.logger.warning('Can\'t find node named %s' % parent_string)
            return []
    
    def filelist_transform(self,fl):
    
        o_list = []
        batfound = None
    
        for f in fl.split('\n'):
            ftype = self.type_for_dtfile(f)
            if ftype == 'bat':
                if batfound is True:
                    ftype = 'bat2'
                else:
                    ftype = 'bat1'
                    batfound = True
            t_d = {'file': f, 'type': ftype}
            o_list.append(t_d)
    
        tmp_l=[i['type'] for i in o_list]
        for i in range(len(o_list)):
            if tmp_l.count(tmp_l[i])> 1 and o_list[i]['type']!='unknown':
                o_list[i]['type']='unknown'
                tmp_l[i]='unknown'
    
        return o_list
    
    
    def type_for_dtfile(self,filename):
    
        known = set(['sae', 'bat', 'tss',
                     'alloc', 'bts', 'cell',
                     'ipconn', 'sigtran'])
        try:
            t_type = re.search('([a-z]+)_.*',
                               os.path.basename(filename).lower()).group(1)
        except:
            t_type = 'unknown'
        if t_type in known:
            return t_type
        else:
            return 'unknown'
