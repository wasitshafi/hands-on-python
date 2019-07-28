num = int(input("Enter value of n : "))
numCopy = num
count = 0

while(num):
   num = num & num -1
   count = count + 1

print("Total no of 1's in", numCopy, "is ", count)  
