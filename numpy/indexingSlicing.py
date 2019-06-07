import numpy as np

a = np.arange(20).reshape(4, 5)

print ("a = ", a)

print ("\nFirst row = ", a[0])
print ("Second row = ", a[1])
print ("Third row = ", a[2])
print ("Fourth row = ", a[3])

#If you want to select a column, you need to add : before the column index.

print ("\n\nFirst column = ", a[:,0])
print ("Second column = ", a[:,1])
print ("Third column = ", a[:,2])
print ("Fourth column = ", a[:,3])
print ("Fifth column = ", a[:,4])

print ("a[2,:1] = ", a[2,:3]) # it means select from row 2 the next 3 values, i.e: 10,11,12 

input("press any key to exit.")