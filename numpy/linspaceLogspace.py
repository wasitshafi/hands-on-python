#Linspace gives evenly spaced samples.
#numpy.linspace(start, stop, num, endpoint)

#Start: Starting value of the sequence
#Stop: End value of the sequence
#Num: Number of samples to generate. Default is 50
#Endpoint: If True (default), stop is the last value. If False, stop value is not included.
import numpy as np


a = np.linspace(1, 5 , num = 10) # its used to create evenly spaced arrays i.e. it simply means u have to print
                                 #  total 10 numbers from 1 to 5 and the difference between each of them must be same
print (a)

#LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.
b = np.logspace(3.0, 4.0, num=4)

print ("b = ", b)                   #?? for mor info  read : https://www.guru99.com/numpy-linspace-logspace.html
print ("item size = ", b.itemsize)  #??
