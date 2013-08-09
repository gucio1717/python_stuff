import mymod

mymod.fun1()
mymod.fun2("Something")

short = mymod.fun1 # without ()

def aa( a ):
    print type(a)
    a()

aa( short )
print type(short)

short()

variable = 10

print "globals: ", globals()
print "locals: ", locals()

print "dir mymod: ",dir(mymod)

'''
print"\n---P1\n"

print globals()

print"\n---P2\n"

print locals()
'''
