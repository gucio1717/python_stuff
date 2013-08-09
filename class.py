class A:
    pass

class B(object):
    pass

a=A()
print "A class:",type(A),", a object:", type(a)
print dir(a)
print "====="
b=B()
print "B class:",type(B),", b object:", type(b)
print dir(b)
















"""
class MyClass:
    def __init__(self, a):
        self.data=a
        
    def f(self):
        print "hi from x"

x=MyClass(4)
xf=x.f
print type(x.f)
xf()
"""
