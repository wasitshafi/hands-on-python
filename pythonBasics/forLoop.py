for x in "The quick brown fox jumps over to the lazy dog. Tit for tat.":
    print (x, end= " ")

fruits = ["apple", "banana", "cherry", "mango", "orange", "grapes", "pears", "pineapple"]
print ("\n")

for x in fruits:
  print(x) 
else:
  print ("bye...\n\n")
print ("range(6)=", end="")
for x in range(6): # 0 to 5
    print(x, end=" ")
print ("\n")

print ("range(3,10) = ", end="")
for x in range(3,10):
    print (x, end=" ")
print ("\n")

print("range(5, 20, 2) ", end="")
for x in range(5, 20, 2):
    print (x, end=" ")
print ("\n")


n = int(input("Enter no of line you want :"))

for i in range(0,n):
  for j in range(0, i):
    print ("*", end="")
  print("")
