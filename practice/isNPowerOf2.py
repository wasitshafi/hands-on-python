# For more info : https://prismoskills.appspot.com/lessons/Bitwise_Operators/Check_power_of_2.jsp
num = int(input("Enter integer (n >= 0) : "))
if(num & (num - 1) == 0):
    print("Yes ", num, " is power of 2.")
else:
    print("No ", num, " is not power of 2.")
