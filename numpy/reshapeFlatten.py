import numpy as np

a = np.arange(12)
print ("a : ", a)
print ( "shape of a : ", a.shape)

# here 'a' has 12 elements so we can reshape so to use all 12 elements ie we can reshape like (2,6),(3,4),(4,3),(6,2)(12,1)...
a = a.reshape(3, 4) # we have to reshape as there must be exactly the same elements for the new array... 
print ("\n\na : ", a)
print ( "shape of a : ", a.shape)

#creating a new array using arange() and reshape like
b = np.arange(0, 15).reshape(3, 5)
print ("\n\nb : " , b)
print ("shape of b : ", b.shape)


#The flatten() function is used to get a copy of an given array collapsed into one dimension. 'C' means to flatten in row-major (C-style) order. 'F' means to flatten in column-major (Fortran- style) order. 'A' means to flatten in column-major order if a is Fortran contiguous in memory, row-major order otherwise
d = b.flatten() #by default its row major i.e: flatten(order = 'C')
e = b.flatten(order ='F')
f = b.flatten(order = 'A')

print ("d = ", d)
print ("e = ", e)
print ("f = ", f)
