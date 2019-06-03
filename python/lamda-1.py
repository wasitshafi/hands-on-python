#A lambda function can take any number of arguments, but can only have one expression.
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

f = lambda x, y : x + y

n1 = int(input("Enter a number : "))
n2 = int(input("Enter a number : "))

print ( "sum = " , f(n1,n2))
