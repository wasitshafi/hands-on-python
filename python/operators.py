"""
LIST OF OPERATORS :
1) Arithmetic operators(+, -, *, /, %, **, //)
2) Assignment operators(=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)
3) Comparison operators(==, !=, >, <, >=, <=)
4) Logical operators(and, or, not)
5) Identity operators(is, is not)
6) Membership operators(in, not in)
7) Bitwise operators(&, |, ^, ~, <<, >>)
"""

print ("2 ** 3 = ", 2**3)
print ("5 / 3  = ", 5 / 3)
print ("5 // 3 = ", 5 // 3)
print ("5 % 3  = ", 5 % 3)
print ("\n")

# as here MSB represents the sign bit
#        60 = 0011 1100 
# ~60 = -61 = 1100 0011 Inverts all bits

print ("~60 = ", ~60)
print ("1024 >> 2 = ", 1024 >> 2) # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print ("2 ** 3 = ", 1024 ^ 1027, end = "\n\n")

print ("5 is 5 = ", 5 is 5)
print ("5 is not 5 = ", 5 is not 5, end = "\n\n")

fruits =['Apple', 'Mango', 'Orange', 'Banana', 'Grapes']
print ("fruits = ", fruits)
print ("\"Apple\" in fruits = ",  "Apple" in fruits)
print ("\"Apple\" not in fruits = ", "Apple" not in fruits)
print ("\"Onion\" in fruits = ", "Onion" in fruits)
print ("\"Onion\" not in fruits = ", "Onion" not in fruits)
