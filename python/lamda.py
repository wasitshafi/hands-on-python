def func(n):
	return lambda a : a * n

double = func(2)
triple = func(3)
quad = func(4)

num = int(input("Enter a number : "))

print ("Double of ", num , " is : ", double(num))
print ("Triple of ", num , " is : ", triple(num))
print ("Quad of ", num , " is : ", quad(num))