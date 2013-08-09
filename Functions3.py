def simple_lambda(b):
   return lambda x:x+12+b

def complex_lambda(n,m):
    o=simple_lambda(n)
    f=m+2
    #o=(lambda x:x+18)
    #print type(o)
    return lambda x,y:(lambda x:x+m)(o(9))*x-(y*f)

h=complex_lambda(6, 14)
print h(20, 100)
