#integer, long, float
var_1 = 123
var_2 = 123L # add L!
var_3 = 12.34
var_4 = 1.2e2
var_5 = 1.2e-200
print "\n---Different numbers---\n"
print 9**.5

print `var_1 ` + " " + `var_2`  

print var_2
print var_3
print var_4
print var_5


var_1 += 4 # var_1 = var_1 + 4
print var_1
var_1 -= 3 # var_ = var_1 - 3
print var_1


var_1 = var_4 / var_5
print var_1
print "\n---Multiple assignment---\n"
var_1 = var_2  = var_5


print var_1
print var_2

#arithmetic operations
# + - * ** / %
var_1 = 12
var_2 = 5

print "\n---Divisions---\n"
print var_1 / var_2 # 12 / 5 -> 2

var_1 = 12.0
var_2 = 5.0

print var_1 / var_2 # 12 / 5 -> 2.4

print "\n---Complex---\n"
var_1 = 1j   #use j not i!
var_2 = 5+8J # size of 'j' doesn't matter

print var_1
print var_1 * var_1

print var_2
print var_2.real
print var_2.imag
#'''
