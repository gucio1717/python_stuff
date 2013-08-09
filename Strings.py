var_1 = "I'm a random text."
var_2 = 'I\'m not a random text.' #backslash as an escape character
                                  # also i.e "She said\"hello\""

print var_1
print var_2


var_3 = "I'm"
var_4 = 'a combination.'
var_5 = 5

var_6 = (var_3 + " " + var_4  + "aaaa") * var_5
print var_6

var_6 = var_3 + var_4
print var_6

print var_3 * 3 #prints var_3 three times

#we can read string elements through index
print var_1[2], var_1[7]

#but we can not write into string through index
#var_1[2] = 'Q'#error

#unicode
uni = u"a \uFC41 \uFC42 -25\u00B0C \u2603 \u2622 \u2601"
print uni

#raw

raw = r'This is \n raw string'
nraw = "This is not \n raw string"
print raw
print nraw
