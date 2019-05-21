import time as t

start = t.time()
for i in range (10000000):
 print (i, end = "  ")
print ()
print ("Time taken to print from 0 to 1000000 is : ", ( t.time() - start ) * 10000, "ms.")  #in miliseconds
# print ("Time taken to print from 0 to 1000000 is : ", (t.time() - start ), "sec.")  #in seconds 
input("Press any key to exit...")