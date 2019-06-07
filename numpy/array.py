import numpy as np

def PRINT(arr):
    for i in arr:
        print (i, end = "  ")

npArray1 = np.array([11, 22, 33, 44, 55]) #1D Array
print ("\nArray : ", npArray1)
print ( "Array (using iterator) : ", end = "") # as print statement executes from right to left
PRINT(npArray1)
print ("\nShape of Array is : ", npArray1.shape)
print ("Dimension of Array is : ", npArray1.ndim)
print ("Data type  of Array is : ", npArray1.dtype)
print ("Total no of elements is : ", npArray1.size)
print ("Size of each array item is : ", npArray1.itemsize)
print ("Array Size is : ", npArray1.size * npArray1.itemsize, " Bytes.", end = "\n\n")
print ("Array last element is :", npArray1[-1])
print ("Array second last element is :", npArray1[-2])
print ("Array third last element is :", npArray1[-3])

npArray2 = np.array([[1, 2, 3],
                     [4, 5, 6]])       #2D Array of order 2 X 3
print ("\nArray : ", npArray2)  
print ( "Array (using iterator) : ", end = "")
PRINT(npArray2)                  #1D Array
print ("\nShape of Array is : ", npArray2.shape)
print ("Dimension of Array is : ", npArray2.ndim)
print ("Data type  of Array is : ", npArray2.dtype)
print ("Total no of elements is : ", npArray2.size)
print ("Size of each array item is : ", npArray2.itemsize)
print ("Array Size is : ", npArray2.size * npArray2.itemsize, " Bytes.", end = "\n\n")

    
#3d array of order 2X2X3
npArray3 = np.array([
                     [[1, 2, 3],
                         [4, 5, 6]],
                     [[7, 8, 9],
                      [10, 11, 12]]
])
print ("\nArray : ", npArray3)
print ( "Array (using iterator) : ", end = "")
PRINT(npArray3)                  #3D Array
print ("\n\n\narray[0] : ", npArray3[0])
print ("array[0][1][2] : ", npArray3[0][1][2])
print ("array[1][1] : ", npArray3[1][1])

print ("\nShape of Array is : ", npArray3.shape)
print ("\nShape of Array is(using iterator) : ", end = "")
PRINT(npArray3.shape)
print ("\n\n\nDimension of Array is : ", npArray3.ndim)
print ("Data type  of Array is : ", npArray3.dtype)
print ("Total no of elements is : ", npArray3.size)
print ("Size of each array item is : ", npArray3.itemsize)
print ("Array Size is : ", npArray3.size * npArray3.itemsize, " Bytes.", end = "\n\n")

myList = [11, 22, 33, 44, 55, 66]
npArray3 = np.array(myList)

for i in npArray3:
    print (i, end = "  ")
	
input("\n\nPress any key to exit...")