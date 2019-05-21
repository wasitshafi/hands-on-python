import numpy as np

npArray1 = np.array([1, 2, 3])
print ("Numpy array is nparray is : ", npArray1)  #1D Array

print ("type = ", type(npArray1))
print ("shape = ", npArray1.shape)
#print ("dtype = ", dtype(npArray1))

npArray2 = np.array([[1, 2, 3], [4, 5, 6]])       #2D Array of order 2 X 3
print ("Numpy array is nparray is : ", npArray2)

myList = [11, 22, 33, 44, 55, 66]
npArray3 = np.array(myList)
for i in npArray3:
    print (i, end = "  ")

input("press any key to exit")