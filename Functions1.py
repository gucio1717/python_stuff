import math

print math.cos.__doc__

def fHello ():
    "fHello docstring: Function prints 'Hello world'"
    print ("Hello World!\n")


def printData ( person, phoneNo ):
    """Another way of setting a docstring

    It also works!!
    """
    print person + "'s phone number is " + str(phoneNo)

print "\n---P1\n"
#Important warning: The default value is evaluated only once (example at the end of the file)
def printData1 ( person = "No name", phoneNo = 0 ):
    print person + "'s phone number is " + str(phoneNo)

fHello()
printData( "Mark", 313438 ) #required arguments
printData( phoneNo = 122345, person = "John" ) # keyword arguments #Notice the order of arguments!!!
printData1() #default arguments



#print of docstrings
print "\n---P2\n"
print fHello.__doc__
print printData.__doc__

#Important warning: The default value is evaluated only once
def f( a, L=[]):
    #print "fun", L
    L.append(a)
    return L

print "\n---P3\n"
print f(1)
print f(2)
print f(3)
lst = [7,8,9]
print f(4, lst)
#print L
''
my_list = f(4)
print my_list

my_list.append(5)
print f(6)

my_list1 = my_list

my_list1.append(7)
print my_list
print f(10)
''
def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f1(1)
print f1(2)
print f1(3)

lst = [7,8,9]
print f1(4, lst)
'''
lst1 = lst
lst1.append(4)
print lst
'''

'''
l = [1,2]
del l
print type(l)
l.append(4)
print l
'''
