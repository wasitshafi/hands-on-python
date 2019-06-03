def sum(x = 10,y = 20):
    return x + y

x = int(input("Enter a number : "))
y = int(input("Enter a number : "))

s = sum(x,y)

print (x , "+" , y , "=" , s)
print ( "sum(10,20) using default arguments : " , sum())