str = input("Enter string (More than 5 characters) : ")

print ("String lenght is : ", len(str))

# CTM : In range function the right most value is excluded so we don't use 'len(str) - 1' .
print ("\n\n")
print ("str = ", end = "")
for i in range(0, len(str)): # at the end of string there is no null character to point that the string has finished
	print(str[i], end = "")

print ("\n\n")
print ("str = %s"%(str))
print ("str[0]  : ", str[0])
print ("str[:]  : ", str[:], end = "\n\n")

print ("str[0:]  : ", str[0:])
print ("str[4:]  : ", str[:4], end = "\n\n")
print ("str[2:5]  : ", str[2:5])

# str[0] = 'a' will give an error although you can assign a new string to a variable as  str = "the quick"

print ("str * 2 = ", str * 2, end="\n\n")
print ("str * 3 = ", str * 3, end="\n\n")
print(r'C://python37') # prints C://python37 as it is written  plz refer :https://www.javatpoint.com/python-strings 

id = int(input("Enter student id : "))
marks = float(input("Enter student marks : "))
name = input("Enter student name : ")

print ("Name = %s Id = %d Marks =%f "%(name, id, marks)); # don't forget the terminator at the end and there is no comma between them

#input("Press any key to exit.")