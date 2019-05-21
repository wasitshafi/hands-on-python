import numpy as np

a = np.arange(6)
print ("a = ", a)

b = np.arange(7, 10)
print ("b = ", b)
h = np.hstack((a, b)) # don't forget double parenthesis
print ("h = ", h)

#v = np.vstack((a, b)) #  this will be error as the 'a' contains 6 elements and 'b' contains only 3 elements 
                       # for vertical stack the no. of  elements must be same in both the array in case of dimension is 1
b1 = np.arange(10, 16)
v = np.vstack((a, b1))

print ("\n\na = ", a)
print ("b1 = ", b1)
print ("v = ", v)

c = np.arange(24).reshape(4, 6)  # 4 * 6 = 24
print ("\n\nc = ", c)



# there is some error in the below  lines
#b = np.hstack((c, 2))               # we have to divide in such a way so that it must be exactly partitioned
#print ("b(after hstack(2) ) = ", b)  
#c = np.vstack((c, 3))
#print ("c(after hstack(3) ) = ", c)