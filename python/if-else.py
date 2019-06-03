x = int(input("Enter a positive number."))
if x < 0 : print (x, " is not a positive number.") # short hand if

print (x ," is even.") if x % 2 == 0 else print (x, " is odd.") # short hand if-else


a = int(input("\n\nEnter a number."))
b = int(input("Enter a number."))

print ("Both numbers are equal.") if a == b else  print ( a ," is greater than ", b) if a > b else print ( b, " is greater than ", a )