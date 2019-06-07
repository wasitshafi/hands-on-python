#Numpy matrices are strictly 2-dimensional, while numpy arrays (ndarrays) are N-dimensional. 
#Matrix objects are a subclass of ndarray, so they inherit all the attributes and methods of ndarrays.

#The main advantage of numpy matrices is that they provide a convenient notation for matrix multiplication: 
#if a and b are matrices, then a*b is their matrix product.

import numpy as np

a = np.mat('1 2 3 4; 5 6 7 8 ;9 10 11 12')
b = np.mat('13 14 15 16; 17 18 19 20; 21 22 23 24; 25 26 27 28')

print ("a = ", a)
print ("\nb = ", b)
print ("\na * b = ", a * b)

# same using array
x = np.arange(1, 13).reshape(3, 4)
y = np.arange(13, 29).reshape(4, 4)

print ("x = ", x)
print ("\ny = ", y)
z = np.dot(x, y) # using numpy
w = x.dot(y)

print ("z(x * y)  = ", z)
print ("w(x * y)  = ", w)

# CTM : a*b is simply the multiplication of each corresponding element of 2 array

print ("\nx + y = ", x * y)
print ("\nx - y = ", x * y)
print ("\nx / y = ", x * y)
