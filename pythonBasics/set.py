#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
fruits1 = {"Apple", "Mango", "Oranges", "Grapes"}
fruits2 = {"Oranges", "Banana", "Pears", "Grapefruit", "Plums"}
# using the update() method to add multiple items:

print ("fruits1 = ", fruits1)
print ("fruits1 = ", fruits2)
fruits1.update(["newfruit1", "newfruit2", "newfruit3"])
print ("After updating fruits1 = ", fruits1 )
print ("len(fruit1) = ", len(fruits1))

print("Printing using for loop friuits1 = ", end="")
for f in fruits1:
    print(f, end = "  ")


