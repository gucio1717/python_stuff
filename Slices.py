text = 'Slicing test'

print "text is:",text
print
print "text[1]",text[1]
print "text[1:2]",text[1:2]
print "text[1:3]",text[1:3]
print "text[1:5]",text[1:5]
print "text[3:]",text[3:]
print "text[:6]",text[:6]

print "---P1"

print "text[-1]",text[-1]
print "text[-1:-3]",text[-1:-3]
print "text[-3:-1]",text[-3:-1]
print "text[2:-3]",text[2:-3]

print "---P2"
print text[1:5:2]
print text[::2]
print text[4::2]
print text[-1:-3:-1]#text[-1:-3]


#print[:]
print text[::]
print text[::-1]
print text[::-2]

print "---P3"
my_tuple = [1, 2, 3]
my_list = [4,5,6,7,8,9]

print my_tuple
print my_list

#my_list[1:3] = my_tuple
my_list[2:3] = my_tuple


print "aaa", my_list
#my_list[2:5] = my_tuple
#print my_list


my_list1 = [4,5,6,7,8]
my_list1[::2] = my_tuple
print my_list1
