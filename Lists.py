my_todo = [ 'reply to an e-mail', 'fiX bug no. 551', 42 ]

print my_todo[1]
print my_todo[2]


tmp = []
print type(tmp)
tmp = 1
print type(tmp)


my_todo[2] = my_todo[2] - 2
print my_todo[2]

#print my_todo[1][2]
#my_todo[1][2] = 'x'

other_list = ['text', 23]
my_todo.append( other_list )
print "my todo:",my_todo
print my_todo[3][0][1]

#'''

#how long / how many things got my todo list
print len(my_todo)

#append, insert
my_todo.append("new item")
print len(my_todo)

print min(my_todo)
print max(my_todo)
#'''

print "\n---List operations---\n"
#sort, reverse
print my_todo
my_todo.sort()
print "sort"
print my_todo
my_todo.reverse()
print my_todo

element = 'reply to an e-mail'
#element = 'text'
#element = other_list #str()

if element in my_todo:
    print element + " is in the list"

print "\n---Matrix---\n"
#list as matrix
matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
print matrix
print matrix[1][1]

for row in matrix:
    for i in range(3):
        print row[i],
    print


lst = [1,1,2,3,4,3,4,2]

szukany = 3

if szukany in lst:
    print szukany
