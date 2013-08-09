con_1 = True #case sensitive
con_2 = False

if con_1 and not con_2:
    print 'True'
else:
    print 'False'

print "---"

var_1 = 4
var_2 = var_3 = 5

if var_1 < var_2 == var_3 < 6:
    print 'OK'

var_1 = 0
var_2 = -4

print "---"

if var_1:
    print 'var_1 is true'
if var_2:
    print 'var_2 is true'


print "---"

strings = ['c++', 'perl', 'java', 'python', 'sql']

if "c++" in strings:  # notice ':' !
    print 'c++ is in the strings'

#-----

if "c#" in strings:
    print 'c# is in the strings'
else:
    print 'c# is not in the strings'

#-----

print "---"

#indents ARE very IMPORTANT
for i in strings:
    print i
    if 'p' in i:
        print 'p'
        if 'e' in i:
            print 'e'
print 'loop end'
