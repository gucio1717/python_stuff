import sys

print sys.argv[0]
#print sys.argv[1]

str1 = raw_input("Enter some data: ") # "text" * 5
print str1


str2 = input("Enter some numeric data: " )# "text" * 5
print str2

fo = open("file_name.txt", "wb")
fo.write( "I'll be printed inside some file\n" )
input()
fo.write( "I'll be printed inside some file2" )
fo.close()

