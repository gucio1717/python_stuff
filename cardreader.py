import re

operator_map = {r"::*:::*::": "+",
                r"::::*::::": "-",
                r"*:*:::*:*": "*",
                r":::***:::": "/"}

def validate (card):
    for i,line in enumerate(card):
        if ((i==0 or i==4) and not re.match("\:{9}",line)):
            print ("start stop wrong", line)
            return False
        if ((i==1 or i==3) and not (re.match(":*\*{1}:*",line) and re.match("[:*]{9}",line))):
            print ("not valid number", line)
            return False
                               
    return True

def calculate (card):
    var1= str(card[1].find("*")+1)
    var2= str(card[3].find("*")+1)

    try:    
        operator = str(operator_map[card[2]])

    except KeyError:
        print "Invalid operator", card[2]
        return -1
    
    print "Operation: ", var1, operator, var2
    print "Result: ", eval(str(var1+operator+var2))
    


    
    
