phrase="Ka jak"

stripped_phrase=list(phrase.lower().replace(" ",""))
ph_length=len(stripped_phrase)
result=0

for i,string in enumerate(stripped_phrase):
    if string != stripped_phrase[-(i+1)]:
        break
else:
    result = 1
    
print result

    


    





