print ("Enter an integer : ")
num = int(input()) # by default input read as string so use int() to convert that into integer

if( num % 2 == 0):
    print(num,end="")
    print(" is even.")
else:
    print(num,end="")
    print(" is odd.")
