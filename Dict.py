countries = { 'ES' : 'Spain',
              'FR' : 'France', 'DE' : 'Germany', 'PL' : 'Poland' }

print countries['DE']
#print countries['Poland'] #wrong

print "values:",countries.values()
print "keys:",countries.keys()
print "keys list type", type(countries.keys())
s=sorted(countries.keys())

print "sorted keys:",sorted(countries.keys())
print "key-value pairs:",countries.items()

'''
#new in 2.7 - dictionary view objects
print "---"
print countries.viewvalues()
print countries.viewkeys()
print countries.viewitems()

print countries.viewvalues() - countries.viewkeys() #creates a set - properties of dictview
'''
print "remove DE, add CH and reassign FR"
del countries['DE']
countries['CH'] = 'Switzerland'
countries['FR'] = 'Belgium'


print countries.values()
print countries.keys()

print "check if DE is in countries"
print "is?",'DE' in countries
print "is not?",'DE' not in countries

'''
print len(countries)
countries.clear()     # remove all entries in dict
print len(countries)
del countries        # delete entire dictionary
print len(countries)
'''


for a,b in countries: #by default returns keys
    #print type(a), type(b)
    print a, b
    
for a,b in countries.items():
    #print type(a), type(b)
    print a,b

