import logging
import re
from mfw.dataprovider import DataProvider


class SoftwareData(DataProvider):

    def __init__(self, file):
        super().__init__()
        self._file = file
        self.data = {}
        self._state = 0
        self._lineNr = 0


        self.data['source']=self.find_data_type(file)
        self.generate(file)



    def find_data_type(self , file):
        '''
        Check which type of data is provided in the file and return it.
        '''
        _laeipPrintoutHeader = "REGIONAL SOFTWARE UNIT IDENTIFICATIONS"

        result = 'UNKNOWN TYPE'
        with open(file, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line.find(_laeipPrintoutHeader) != -1:
                    result = 'LAEIP'
        return result

    def execute(self):
        return self.data

    def generate(self, file):
        
        self.logger.debug('Software data controller is executed!')
        
        data_type=self.data['source']
        if data_type == 'LAEIP':
            self.parse_LAEIP(file)
        elif data_type == 'UNKNOWN TYPE':
            pass
        else:
            self.logger.error('Incorrect data type.')

        print('Sw data controller is executed!')
        print(data_type)
        
        return "HW_DATA_STRUCTURE"

    def get(self,key):
        if key in self.data.keys():
            return self.data[key]
        else:
            self.logger.error('Missing key: %s' % key)

    def parse_LAEIP(self, file):
        print('parse_LAEIP executed.')
        _laeipPrintoutHeader = "REGIONAL SOFTWARE UNIT IDENTIFICATIONS"

        self.logger.info("Parse LAEIP data from file: %s", file)
        software={}
        with open(file, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if self._state == 0:
                    if line.find(_laeipPrintoutHeader) != -1:
                        self.logger.debug("Printout start at line: %i",
                                          self._lineNr)
                        f.readline()
                        line = f.readline()
                        self._parse_header(line)
                        self._state = 1
                else:
                    tmp = self.analiseLine(line)
                    if not tmp:
                        continue
                    if tmp['SUNAME'] not in software:
                        software[tmp['SUNAME']] = []
                    software[tmp['SUNAME']].append(tmp)
                self._lineNr += 1

        self.logger.info("Printout parsing complete (%i records).",
                         len(software))
        while software:
            key,value=software.popitem()
            self.data[key]=value


    def _parse_header(self, line):
        col = []
        pos = 0
        a = re.findall('\w+[ ]*', line)
        for match in a:
            col.append({'name': match.rstrip(),
                        'a': pos,
                        'b': pos + len(match)})
            pos += len(match)
        self.columns = col
        self.logger.debug('Columns: ' + str(self.columns))

    def analiseLine(self, line):
        line.strip()
        if len(line) < 3:
            return None
        if line.find("END") > -1:
            self.logger.debug("Printout end at line: %i", self._lineNr)
            self._state = 0
            return None

        buf = {}
        for col in self.columns:
            buf[col['name']] = line[col['a']:col['b']].strip()

        if buf['BLOCK'] == '':
            # if the field is empty, use name from _prev_rec line
            if self._prev_rec is not None:
                buf['BLOCK'] = self._prev_rec['BLOCK']
            else:
                self.logger.error("Can't resolve block name at \
line %i\nLINE: %s", self._lineNr, line)
                raise Exception("Can't resolve block name at \
line " + str(self._lineNr) + "\nLINE:" + line)
        self._prev_rec = buf
        return buf
