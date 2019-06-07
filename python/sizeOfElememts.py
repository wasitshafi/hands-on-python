import sys

array1 = ["0", "1", "2", "3", "4"]
array2 = range(5)
print ("\narray1 = ", array1)
print ("\narray2 = ", array2)

print ("sys.getsizeof(3) = ", sys.getsizeof(3), "bytes")
print ("sys.getsizeof(3.4) = ", sys.getsizeof(3.4), "bytes")
print ("sys.getsizeof(\"h\") = ", sys.getsizeof("h"), "bytes")
print ("sys.getsizeof(\"hello\") = ", sys.getsizeof("hello"), "bytes")
print ("sys.getsizeof(array1) = ", sys.getsizeof(array1), "bytes")

print ("sys.getsizeof(array2) = ", sys.getsizeof(array2) * len(array2), "bytes")
input("Press any key to exit...")