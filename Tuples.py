#Two different ways of defining a tuple
#my_tuple = ( 'text', 'another text', 321)
my_tuple = 'text', 'another text', 321

print my_tuple
print my_tuple[0]

#my_tuple[2] = my_tuple[2] + 3
#my_tuple.sort()
#my_tuple.append('add')

var_1, var_3, var_test = my_tuple
print var_1
print var_3

#var_1, var_2 = my_tuple


#creating an empty and one element tuple
empty = ()
one = 'element',    # notice the comma!
print len(empty)
print len(one)
empty=(1,"text1")
print type(empty)
print len(empty)
print empty

print "text" in my_tuple

