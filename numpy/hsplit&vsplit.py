import numpy as np

c = np.arange(24).reshape(4, 6)  # 4 * 6 = 24
print ("\n\nc = ", c)


#there is some error in the below  lines
b = np.hsplit(c, 2)               # we have to divide in such a way so that it must be exactly partitioned
print ("b(after hsplit(2) ) = ", b)  
c = np.vsplit(c, 2)
print ("c(after vsplit(3) ) = ", c) 