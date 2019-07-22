#import module(onlyFunction&Variables) " or use the below easy way " 
import platform  # this is a built in module

import moduleOnlyFunctionVariables as m  # 'm' is alias for moduleOnlyFunctionVariables

#to import only some part from module use 'from moduleOnlyFunctionVariables import count
#from moduleOnlyFunctionVariables import sum, multiply, count
#When importing using the from keyword, do not use the module name when referring to elements in the module. Example: 'm.sum' instead of that use directly  sum()

print ( "10 + 20 = ", m.sum(10, 20))
print ( "value of count = ", m.count, end = "\n\n")

print ( "10 * 20 = ", m.multiply(10, 20))
print ( "value of count = ", m.count, end = "\n\n")

print ( "10 - 20 = ", m.difference(10, 20))
print ( "value of count = ", m.count, end = "\n\n")

print ( "10 / 20 = ", m.division(10, 20))
print ( "value of count = ", m.count, end = "\n\n")

print ( "10 % 20 = ", m.modulus(10, 20))
print ( "value of count = ", m.count, end = "\n\n")

print ("your platform is  : ", platform.system(), end = "\n\n")

print("dir(m) = ", dir(m)) # ist all the function names (or variable names) in a module#

print("dir(m) = ", dir(platform)) # ist all the function names (or variable names) in a module#

#for i in dir(m):  # or print using for loop
# print (i, end = "")