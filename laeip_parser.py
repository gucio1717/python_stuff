######### ERICPOL laeipLoader.py  #############
#
# author: eszcmic
#
# Class used to load software from LAEIP printout
#
##############################################
# Date       Version  Description
#
#
# 09.04.2013 0.3.1    Update to sdist + some unittest
# 06.03.2013 0.3      Doesn't crash when there is problem with the file
# 22.02.2013 0.2      First version
#
##############################################


import sys, logging

class LaeipDtLoader:
        # state = ('TRASH','PRINTOUT') States used by class
        
        _laeipHeader = "REGIONAL SOFTWARE UNIT IDENTIFICATIONS"
        
        def __init__(self, file):
                self.state = 'TRASH'
                self.file = file
                self.lineNr = 0
                self.last = None
                self.soft = []

                #Search through the file and find printout lines. Then analise each line.'
                try:
                        print("Opening LAEIP file:", self.file)
                        f = open(self.file, 'r')
                except:
                        print("Can't open LAEIP file:",self.file)
                        return
                for line in f:
                        if self.state == 'TRASH':
                                self.lookForHeader(line)
                        else:                            #We are analysing printout
                                tmp = self.analiseLine(line)
                                if tmp: 
                                        self.soft.append(tmp)
                        self.lineNr += 1
                f.close()


        def lookForHeader(self, line):
                if line.find(LaeipDtLoader._laeipHeader) != -1:
                        self.state = 'PRINTOUT'
                        logging.debug("\nlaeipLoader PRINTOUT start at line: %i", self.lineNr)
                        
                        
        def analiseLine(self,line):
                line.strip()
                if len(line) < 3:
                        return None
                if line.find("BLOCK",0,6) != -1:
                        return None
                if line.find("END",0,3) != -1:
                        self.state = 'TRASH'
                        logging.debug("laeipLoader PRINTOUT end at line: %i", self.lineNr)
                        return None
         
                buf = {}
                buf['block'] = line[0:8].strip()
            
                if not buf['block']:
                        if self.last != None: #if the field is empty, use name from previous line
                                buf['block'] = self.last['block']
                        else:
                                print("ERROR: Can't resolve block name at line "+str(self.lineNr)+"\nScanning stopped")
                                print("LINE: "+line)
                                sys.exit(1)
                
                buf['bn'] = line[8:14].strip()
                buf['suname'] = line[14:23].strip()
                buf['suid'] = line[23:56].strip()
                buf['sutype'] = line[56:63].strip()
                buf['cno'] = line[63:66].strip()
                buf['prio'] = line[66:].strip()
                
                self.last = buf.copy() #store last line for block number when current line is empty
                return buf
            
        def getSoftRecordStr(self,id):
                if id < len(self.soft):
                        return "%s %s %s %s %s %s %s" % (self.soft[id]['block'],
                                                         self.soft[id]['bn'],
                                                         self.soft[id]['suname'],
                                                         self.soft[id]['suid'],
                                                         self.soft[id]['sutype'],
                                                         self.soft[id]['cno'],
                                                         self.soft[id]['prio'])
                return None

        def __iter__(self):
                for i in self.soft:
                        yield i

        def __len__(self):
                return len(self.soft)

        def __getitem__(self,i):
                return self.soft[i]

import re

f = LaeipDtLoader(r'H:\tmp\LAEIP.log')

#laeip_map = {'GARP2A': [{ 'suname': 'INETR', 'cno': '', 'suid': r'^7/'}, { 'suname': 'RGCONR', 'cno': '', 'suid': r'^7/'}] }

laeip_map = {'INETR':      [{'cno': '', 'suid_reg': r'.*', 'type': 'garp2a'},{'cno': '', 'suid_reg': r'.*', 'type': 'rpp4s' }],
             'default':    [{'cno': '', 'suid_reg': r'^8/', 'type': 'epb1'},  {'cno': '', 'suid_reg': r'^7/', 'type': 'garp2a'}]
             
             
             }
             
#print (laeip_map['GARP2A'][0])             
for a in f:
    #print (a['suname'])
    if 'default' in laeip_map.keys():

        # lets try defaults first
        
        for rptype in laeip_map['default']:
            # try to match suid with regexp
            if re.match(rptype['suid_reg'], a['suid'] ):
                print(a['suname'] + " " + a['suid']+ " " + rptype['type']+ " " + rptype['suid_reg']) 
        
    # then, scan particular SUNAMEs
    
    for x in laeip_map[a]:
    
        if re.match(x['suid_reg'], a['suid']):
            print(a['suname'] + " " + a['suid']+ " " + x['type']+ " " + x['suid_reg'])
            
        
            
#     if a['suname'] in laeip_map.keys():
#         print('Found'+ str(laeip_map[a['suname']]))