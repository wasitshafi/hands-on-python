# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
dict1 = {
    "name":"suzuki",
    "model":"m22x5",
    "year":2015
}

print ("dict1 = ", dict1)
print ("dict1[name] = ", dict1["name"])
print ("len(dict1) = ", len(dict1))

print ("\ndict1.get(\"model\") = " , dict1.get("model"))
dict1["year"] = 2018
print ("\nAfter updating year = " , dict1["year"])

print ("\nPrinting through for loop : ")
for x in dict1:  # or use 'for x in dict1.values()'  or 'for x in dict1.items()' for printing value directly
    print (x , " = ", dict1[x], end=" ")

dict1["color"] = "red"
print ("After adding new item 'color' to dictionary : ", dict1)

k = input("\nEnter a key attibute which you want to find : ")
if k in dict1:
    print ("Key is in dict1")
else:
    print ("Key is not in dict1")

dict1.pop("color")
print ("After  dict1.pop(\"color\") item dictionary(Deleting item using pop()) items are as  : ", dict1)


del dict1("model") # CTM: del is capable of deleting the dictionary as whole where pop is not capable.
print ("After del dict1(\"model\") item dictionary(Deleting item using del)  items are as  : ", dict1)



