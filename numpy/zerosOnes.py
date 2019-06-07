import numpy as np

#syntax
#numpy.ones(shape, dtype=float, order='C') # 'C' for row major order(default) and 'F' for column major order 

print ("zeros((2,2)) : ", np.zeros((2,2)) ) # don't forget that 2 parenthesis
print ("zeros(4) : ", np.zeros(4))
print ("ones(4) : ", np.ones((4), dtype = np.float16))

x = np.zeros((2, 4,3), dtype = np.int16 , )
print ("zeros((2, 4,3))", x)

x = np.ones((2, 4,3), dtype = np.float16 , )
print ("ones((2, 4,3))", x)

