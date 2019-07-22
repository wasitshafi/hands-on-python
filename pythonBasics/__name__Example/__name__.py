import file1 as f

def fun2():
 print("__main__(from fun2) = ", __name__)

def fun1():
 print("__main__(from fun1) = ", __name__)
 fun2()

if (__name__ == "__main__"):
 print("__main__(from mian) = ", __name__)
 fun1()
 f.fun3()

   
