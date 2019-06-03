# The open() function takes two parameters; filename, and mode.
# There are four different modes r(read), a(append), w(write), x(create)

f = open("hello.txt")
print ("Reading whole file content : ", f.read())
f.close()

f = open("hello.txt")
print ("Reading only first 10 character of file : ", f.read(5))
f.close()

f = open("hello.txt")
print ("\n\nReading first line of file : ", f.readline())
print ("Reading second line of file : ", f.readline())
print ("Reading third line of file : ", f.readline())

print ("Notice it prints 2 new line between above 3 line as one \\n is inbulit in print function and another is the \\n from file itself.")
f.close()

