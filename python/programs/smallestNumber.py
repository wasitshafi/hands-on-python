num1 = 10
num2 = 30
num3 = 50

if num1 < num2:
    if num2 < num3:
        print ("num1 is smallest.")
    else:
        print ("num3 is smallest.")
elif num2 < num3:
    print ("num2 is smallest.")
else:
    print ("num3 is smallest.")
