import re

print "\n---Substitution---\n"
st = '12w::dw::add'
print st
print "substitute any 3 signs followed by ':' (included) with 'x'"
print re.sub('(.{3}):',\1 , st)
print st

print "\n---Mail search---\n"
str1 = "test@gmail.com test2@yahoo.com"
print "String to be searched:", str1
print "Looking for an email"
tst=re.compile("(?P<login>[a-zA-Z][a-zA-Z0-9]*)[@][a-zA-Z]+[.][a-zA-Z]{2,4}$") 
res=tst.search(str1)
#res=tst.match("(?P<login>[a-zA-Z]+[a-zA-Z0-9]*)[@][a-zA-Z]+[.][a-zA-Z]{2,4}")
if res:
    print "my match is:",res.group(0), "login is:",res.group("login")
else:
    print "Provided string does not contain valid email address"

print "\n---Find all occurences---\n"
str2='which foot or hand feel fastest'
print "String to be searched:",str2
findings=re.findall(r'\bf[a-z]*', str2)
print "Search result - all words starting with 'f':",findings




