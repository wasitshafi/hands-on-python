# a module can contain functions , vairable, lists, tuples
count = 0  #here count is a global variable

def sum(x, y):
    global count
    count = count + 1
    return x + y

def multiply(x, y):
    global count
    count = count + 1
    return x * y

def difference(x, y):
    global count
    count = count + 1
    return x - y
def division(x, y):
    global count
    count = count + 1
    return x - y
def modulus(x, y):
    global count
    count = count + 1
    return x - y