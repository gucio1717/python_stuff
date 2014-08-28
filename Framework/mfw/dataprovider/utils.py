'''
Utilities for DT bfg
'''

import os
import glob
import logging
import re


def is_xml(file_path):

    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.xml':
        return True
    else:
        return None


def find_bsc_config_template(base_dir, bsc_config_name):
    '''Find DT template file for given bsc_config_name.
    @param base_dir Path to dir with BSC configurations folders
    @param bsc_config_name Name of the bsc to search
    return dtt_filepath if exists or None
    '''
    parser_ind = bsc_config_name.find('_')
    if parser_ind != -1:
        bsc_name = bsc_config_name[0:parser_ind]
    else:
        bsc_name = bsc_config_name
    dtt_filepath = os.path.abspath(base_dir +
                                   '/' + bsc_name +
                                   '/' +
                                   bsc_config_name +
                                   '.dtt')
    if os.path.isfile(dtt_filepath):
        return dtt_filepath
    else:
        return None


def get_feature_dtt_files(dt_path):
    '''Search for template files in DT feature directory.
    @param dt_path Path to feature directory
    @return Dictionary with feature identifier and files to load'''
    dt_path = os.path.abspath(dt_path)

    if not os.path.exists(dt_path):
        logging.warning("Path doesn't exists: " + dt_path)
        return {}

    dtt_files = {'identifier': os.path.basename(dt_path)}
    for file_path in glob.glob(os.path.abspath(
                               os.path.join(dt_path, '*.dtt'))):
        file_name = os.path.basename(file_path)
        dt_folder_path = os.path.dirname(file_path)
        dtt_files[file_name.split('.')[0]] =\
            os.path.basename(dt_folder_path) + '/' + file_name
    return dtt_files


def get_all_features_dtt(base_dir):
    '''Finds correct DT templates for all features in base_dir.
    @param base_dir Path to dir with all features
    @return list of dtt_files dictionaries'''
    dts = []
    for feature_name in glob.glob(os.path.abspath(
                                  os.path.join(base_dir, '/*'))):
        dt = get_feature_dtt_files(feature_name)
        if len(dt) > 1:
            dts.append(dt)
        else:
            logging.warning("Could not find correct DTT template for \"%s\"",
                            feature_name)
    return dts


def get_all_features_dtt_from_file(features_dir, file):
    '''Load feature names from file and search for their DT templates.
    @param file Path to file with feature names
    @param base_dir Path to dir with all features
    @return list of dtt_files dictionaries'''
    if not os.path.isfile(file):
        logging.warning("File doesn't exist: %s", file)
        return []

    f = open(file, 'r')
    features_list = f.readlines()
    dts = []
    for feature_name in features_list:
        feature_name = feature_name.strip()
        if feature_name:
            dt = get_feature_dtt_files(features_dir + "/" +
                                       feature_name.strip())
            if len(dt) > 1:
                dts.append(dt)
            else:
                logging.warning("Could not find correct DTT \
template for \"%s\"", feature_name)
    return dts


def contains_feature(dts, name):
    '''Check if dts already contains feature template.
    @param dts List of dtt_files dictionaries
    @param name Feature name
    @return Boolean'''
    for dt in dts:
        if dt['identifier'] == name:
            return True
    return False


def get_identifiers_str(dts):
    '''Get all identifiers from dts and returns
    them as string separated with comma.'''
    _list = []
    for dt in dts:
        _list.append(dt['identifier'])
    return ", ".join(_list)


def AxeParser(t_input):
    ''' Checks input list and returns valid MMLs commands with parameters
    as list of dictionaries. '''

    t_l = []
    for i in t_input:
        t_list = i.split(':')
        if len(t_list[0]) == 5:
            item = {'name': t_list[0]}
        t_list[1] = t_list[1][:t_list[1].find(';')]
        t_list = t_list[1].split(',')
        for j in t_list:
            if j.find("=") > 0:
                item[j[:j.find("=")]] = j[j.find("=") + 1:]
            else:
                item[j] = ''
        t_l.append(item)
    return t_l


def FindCommand(dt, name):
    return [i for i in dt if i['name'] == name]


def FindParam(dt, params):
    result = dt
    for i in params.keys():
        tmp_l = []
        for j in result:
            if i in j:
                if params[i] == j[i] or params[i] == '*':
                    tmp_l.append(j)
        result = tmp_l

    return [] if result == dt else result

def ChangeFileName(name):
    name = name.replace('/proj/','x:\\')
    name = name.replace('/','\\')
    return name

def get_all_dt(filelist):
    '''Gets through all the files in filelist
    and returns all lines which appear to be
    valid MML. Print commands, commented lines
    and whitespace are stripped.
    '''
    alldt_l = []
    for l in filelist.split('\n'):
        win=ChangeFileName(l)
        if os.path.isfile(win):
            with open(win) as f:
                data = f.read()
                alldt_l.extend(strip_dt_lines(data))

        else:
            logging.error('File %s not found' % win)

    return alldt_l


def strip_dt_lines(dt_lines):

    tmp_l = re.findall('^\s*[^!]\s*(\w{4}[^pP]:[^\n]+\;)',
                       dt_lines,
                       flags=re.MULTILINE)
    tmp_l = [re.sub('\s', '', i) for i in tmp_l]
    return tmp_l


def split_dt_file(dtfile, marker):
    '''Split text file into parts separated by marker
    return list of strings, each element is file part
    @param dtfile Path to file
    @param marker Regexp which separates file parts'''

    dest_l = []
    tmp_l = []

    with open(dtfile, 'r') as f:
        for line in f:
            _l = line
            tmp_l.append(_l)

            if re.match(marker, _l):

                dest_l.append(''.join(tmp_l))
                tmp_l = []

    dest_l.append(''.join(tmp_l))
    print(dest_l)
    return dest_l


def add_to_rrapi_list(l, addr, apl):

    for a in apl.split(','):

        t_d = {'addr': addr, 'apl': a}

        l.append(t_d)


def get_all_files(master_file):

    t_list = []

    try:
        with open(master_file) as f:
            data = f.read()
    except IOError:
        logging.error('Error opening master file')

    try:
        batfile = (re.search('REFERENCE_BAT_FILE[^/]+([^!\ ]+.sdt)',
                             data)).group(1)
        allocfile = (re.search('REFERENCE_ALLOC_FILE[^/]+([^!\ ]+.sdt)',
                               data)).group(1)
    except:
        logging.error('BAT or allocation file not found in masterfile')
        return ''

    for i in re.findall('[^! ]@dtfile\s+([^\n\s]+\.\w+)', data):
        if re.match('.*ECB_BATFILE_PART\d.*', i):
            t = batfile
        elif re.match('.*ECB_ALLOCFILE_PART1.*', i):
            t = allocfile
        elif re.match('.*ECB_ALLOCFILE_PART2.*', i):
            continue
        else:
            t = i
        t_list.append(t)

    return '\n'.join(t_list)

if __name__ == '__main__':
    pass
