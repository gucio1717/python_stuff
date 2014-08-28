import xml.etree.ElementTree as ET

xmltext = """
<root>
<system>
<nodeinfo apz='21260' nodetype='Evo8200' apzvariant='E16' />
</system>
<rplist>
<rp rp='1' appl='cth' />
<rp rp='2' appl='gph' />
</rplist>
</root>
"""

tree = ET.parse(r'h:\full-dt-gen\bsc011.xml')
root = tree.getroot()

print(root)
s = root.find('system')

print(s)

n= s.find('nodeinfo')

print(n.tag,n.attrib)

rl = root.find('rp_list')

print(rl)

for rp in rl.iter('rp'):
    print(rp.tag, rp.attrib) 

gbip_l = root.find('gbip')

for nsei in gbip_l.iter('nsei'):
    print(nsei.tag,nsei.attrib)
    
cth_et=root.find('ip_cth')
print(cth_et.attrib)
