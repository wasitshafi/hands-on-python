# Basics of Placeholders
print("Hello World, I am {username}, software developer at {companyname}".format(username = 'wasit', companyname = 'VectoScaler'))
print("Hello World, I am {0}, software developer at {1}".format('wasit', 'VectoScaler'))
print("Hello World, I am {1}, software developer at {0}".format('VectoScaler', 'wasit'))
print("Hello World, I am {}, software developer at {}".format('wasit', 'VectoScaler'))
print("Hello World, I am {}, software developer at {}".format('VectoScaler', 'wasit'))

ff = 456456.456456456465
print(ff)
# To print only 2 digits after decimal point

print("{:.2f}".format(ff)) # Read more ar : https://thepythonguru.com/python-string-formatting/