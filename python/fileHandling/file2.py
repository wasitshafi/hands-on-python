f = open("hello.txt", 'a')

#print ("File content are as : ", f.read())

str = input("Enter some text to append on file : ")

f.write(str)
#print ("After writing  into file : ", f.read() )