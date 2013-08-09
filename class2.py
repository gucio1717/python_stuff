class a(object):
    def __init__(self):
        print "class a"

class b(object):
    def __init__(self):
        print "class b"
"""
class z(b):
    def __init__(self):
        print "class z"
"""
class c(a):
    def __init__(self):
        print "class c"
        super(c, self).__init__()

class d(c,b):
    def __init__(self):
        print "class d"
        super(d,self).__init__()

class e(d):
    def __init__(self):
        print "class e"
        super(e,self).__init__()
        
        
def main():
    print "c"
    oc=c()
    print "d"
    print "d mro:",d.__mro__
    od=d()
    print "e"
    print 'e mro:',e.__mro__
    oe=e() 
if __name__=='__main__':
    main()
