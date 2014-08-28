from xml.etree.ElementTree import ElementTree
import re

i = open('H:/CI/TSS.SDT', 'r').read()

cells = re.findall(r'RLDEI:CELL=(.+),', i)
tgs = re.findall(r'RXMOI:MO=RXOTG-(\d+),', i)
# asddddd dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd sasasasasas

a = 'asdjajksj jsdjaskl djaskldjklajdk asjklas jklaj dkla dkaj sdklajdkl ajsdklj aklsdj aklsdj aklsjdaklsj dklasj dklasjdkl'


print (cells)
print (tgs)
# rp_list = list(ElementTree().parse(f).iter('rp'))
# 
# for rp in rp_list:
#     print(rp.attrib['number'])
#     
