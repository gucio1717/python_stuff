print "\n---Figures---\n"
names = ('circle', 'triangle', 'rectangular')
print names, type(names)
figures = set(names)
print figures, type(figures)
lst = [figures]
print type(lst), len(lst)
print "tu",lst

print "circle" in figures
print "ball" not in figures

figures.add('ball')
figures.remove('triangle')
print figures
print "set_1 example"
set_1 = set([26,26])
print len(set_1), type(set_1.pop())
set_1 = set([26])
set_1.add(34)
print "set_1",set_1
print "\n---Set from string---\n"
set_2 = set('lettersnumbers123')

print "set_2",set_2

print "---"
print "set_1-set_2:",set_1 - set_2 # in set_1 but not in set_2  A \ B
#print set_1.difference(set_2)
print set_2 - set_1 # in set_2 but not in set_1  B \ A


print "---"
print set_1 & set_2 # set_1 and set_2
#print set_1.intersection(set_2)

print set_1 | set_2 # set_1 or set_2    A u B
#print set_1.union(set_2)

print set_1 ^ set_2 # A\B u B\A
#print set_1.symmetric_difference(set_2)

print set_1.isdisjoint(figures)

print set_1 | set_2 | figures



print "---"
print (set_1-set_2) < set_1 # test if A is a true subset of B - other possibilities <= >=
