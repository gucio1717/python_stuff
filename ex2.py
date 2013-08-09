phrase="Abcdefghij klmnopqrstuvwxyz"

mapping={"abc":  2,
         "def":  3,
         "ghi":  4,
         "jkl":  5,
         "mno":  6,
         "pqrs": 7,
         "tuv":  8,
         "wxyz": 9,
         "#":    "#",
         }
         
         
translated_phrase=list(phrase.lower().replace(" ","#"))

for letter in translated_phrase:
    for i in mapping.keys():
        rep=i.find(letter)+1
        if rep:
            print str(mapping[i])*rep
            
print translated_phrase

