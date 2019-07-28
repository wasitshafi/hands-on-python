num = int(input("Enter positive integer (n >= 0) : "))
numCopy = num
rem = 0
binary = []    # list
while(num != 0):
 rem = num % 2
 binary.insert(0, rem)
 num = num // 2     # integer division
 

print("Binary equivallent is : ", end = "")
if (numCopy == 0):
    print("0")
else:
    for i in binary:  #CTM: we don't actuall form the binary no in base10 rather we just store the remainder. Note : Check the second part of the same program as well
       print(i, end = "")
