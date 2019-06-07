def func(n):
	return lambda a : a * n

double = func(2) #now double has been assigned an expression a:a*2 as func() return  a lamda expression itself
triple = func(3) # triple = a:a*3
quad = func(4)   # quad = a:a*4

num = int(input("Enter a number : "))

print ("Double of ", num , " is : ", double(num))
print ("Triple of ", num , " is : ", triple(num))
print ("Quad of ", num , " is : ", quad(num))