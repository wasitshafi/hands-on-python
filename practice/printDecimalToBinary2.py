num = int(input("Enter positive integer (n >= 0) : "))
numCopy = num
rem = 0
binary = 0
base = 1

while(num):
 rem = num % 2
 binary = binary + rem * base
 base = base * 10  
 num = num // 2    # integer division

print("Binary equavillent of ", numCopy, " is : ", binary, sep = "")
