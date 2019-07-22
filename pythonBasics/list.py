#List is a collection which is ordered and changeable.
#Allows duplicate members.

fruits = ["Apple", "Mango", "Orange", "Banana", "Grapes"]

print ('fruits = ', end = "")
for f in fruits:
  print (f, end = "  ")

print ("\nlen(fruits) = ", end = ""), print(len(fruits))
print ("fruits[2] = ", end = ""), print(fruits[2])

fruits.reverse()
print ("\nfruits.reverse = ", fruits)

fruits.sort()
print ("fruits.sort = ", fruits)
f = input("\nEnter fruit name which you want to search : ")
if f in fruits:
 print (f + " is in the list of fruits. ")
else:
 print (f + " is not in the list of fruits.")

f = input("\n\nEnter fruit name which you want to append in list : ")
fruits.append(f)
print ("Fruits are as : ", end = "")
for x in fruits:
    print (x, end = "  ")

f = input("\n\n\nEnter fruit name which you want to insert in list : ")
i = int(input("Enter index 0 to " + str(len(fruits)) + " ) " ))
fruits.insert(i, f)   # if give -ve number then it will take mod of that...and if u give greater index then it will behave like a append() i.e: it will simply add new element on the end of list
print ("Fruits are as : ", end = "")
for x in fruits:
    print (x, end = "  ")


f = input("\n\nEnter fruit name which you want to remove from the list : ")
fruits.remove(f)
print ("Fruits are as : ", end = "")
for x in fruits:
    print (x, end = "  ")

print ("\n\n\nRemoving last element from the list by using fruits.pop() : ")
fruits.pop() # removes the last element
print ("Fruits are as : ", end = "")
for x in fruits:
    print (x, end = "  ")


i = int(input("\n\n\nEnter the index of element which you want to remove using pop() : "))
fruits.pop(i)
print ("Fruits are as : ", end = "")
for x in fruits:
    print (x, end = "  ")

i = int(input("\n\n\nEnter the index of element which you want to remove using del: "))
del fruits[i]
print ("Fruits are as : ", end = "")
for x in fruits:
    print (x, end = "  ")
# use 'del fruits' to delete whole playlist
# use 'fruits.clear()' to empties the list

fruits2 = fruits.copy() # just make a copy
                        # use 'fruits2 = fruits' then is fruits2 will only be a reference to fruits, any  changes made in fruits will automatically also be made in fruits1.