num = int(input("Enter a number : "))
numCopy = num
reverseNum = 0

while(num):
 rem = num % 10
 reverseNum = reverseNum * 10 + rem 
 num = num // 10     # integer division
 
print("Reverse of ", numCopy, " is : ", reverseNum)