#for
for i in xrange(10):
    print i

print "---P1\n"

for i in reversed( xrange(10) ):
    print i

print "---P2\n"

for i in xrange(5,15):
    print i

print "---P3\n"

my_list = ['a','b','c']
print my_list
print id(my_list[0])

for x,y in enumerate(my_list):
    print x,y
    print id(y)
    print type(x)


print "---P4\n"

#while

var = 5

while var > 0:
    print var
    var -=1

print "---P5\n"

#Loop control - break, pass, continue

for i in "Python":
    if i == 'h':
        pass
    print i
else:
    print "I'm done"

print "---P6\n"

for i in 'Python':
    if i == 'h':
        break
    print i
else:
    print "I'm done"

print "---P7\n"

for i in "Python":
    if i == 'h':
        continue
    print i
else:
    print "I'm done"
