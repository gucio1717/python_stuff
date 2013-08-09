def varLenghtF( arg1, *arg2 ): #in fact arg2 is a tuple
   print "Output is: "
   print arg1
   print "Tuple content:"
   for element in arg2: 
      print element

varLenghtF( 10 );
varLenghtF( "A", "B", "C" );

print "\n"

#**arg3 - dictionary containing all keyword arguments except for those corresponding to a formal parameter # ** after *
def dictExample(arg1, *arg2, **arg3):
    print arg1

    for element in arg2:
        print element
    print "hash"
    keys = sorted(arg3.keys())
    for key in keys:
        print key, ":", arg3[key]
        print type(key)
    #print arg3['capital']
    #print capital

dictExample( 124, "Tuple1", "Tuple2",
           "Tuple2",
           country='Poland',
           capital="Warsaw", continent="Europe")

################
#print "\n---P1\n"

price = 10;

def addVAT( price ):
    VAT = 23.0/100.0
    #global price
    #price = 0
    price = price + price * VAT
    return price
print "----tuple---"
def modTuple(tple):
   x,y,z=tple
   print x, y, z
   tple2=7,8,9
   tple=tple2
   print tple, tple2
   
tple=(1,2,3)
modTuple(tple)
print tple
print "---/tuple---"
   
print addVAT(price)
print price

for i in range(9):
   i +=2
   print i
   

zm1 = set("111")
print zm1
zm1 = ["aaa"]
print zm1
#
#'''

my_list =[1,2,3]

def addToList( my_list ):
    my_list.append(10)

print my_list
addToList( my_list )
print my_list
#'''
