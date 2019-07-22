#
#
#
#
import inspect

num = 10
def func():
    frame = inspect.currentframe()
    name = inspect.getframeinfo(frame).function
    
    print ("Inside " ,name, "() function")
    string = "The quick brown fox jumps over to the lazy dog. Tit for tat."
    print ("locals() = ", locals(), end = "\n\n")
    print ("globals() = ", globals(), end = "\n\n")

func()
print ("Inside main function")
print ("locals() = ", locals(), end = "\n\n")
print ("globals() = ", globals(), end = "\n\n")