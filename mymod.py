"""this is doc"""
from math import cos



def fun1():
    print "I'm fun1 from mymod module!\n"

def fun2( str ):
    print str + "\n"

def main():
    print "hello, I'm module"

if __name__=="mymod":
    print "i'm being imported!"

if __name__=='__main__':
    main()
