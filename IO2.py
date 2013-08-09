import pprint

print "\n---Powers---\n"
for x in xrange(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4)


print "What was first the {0} or the {1}".format('egg','chicken')
print "What was first the {1} or the {0}".format('egg','chicken')
print "What was first the {arg2} or the {arg1}".format(arg1='egg',arg2='chicken')


print "\n---Powers - formated---\n"
#Printing numbers
for x in range(1,11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)

my_number = 123.65543

print my_number
print "{0:.3f}".format(my_number)


calendar = {'March': 3, 'April': 4, 'May': 5}
for month, number in calendar.items():
    print '{0:10} - {1:10d}'.format(month, number)

print "\n---Calendar---\n"

print calendar
print "here"
pprint.pprint(calendar) #output is sorted
pprint.pprint(calendar, width=15)
print "\n---Matrix---\n"
matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
pprint.pprint(matrix)
pprint.pprint(matrix, width=15)

