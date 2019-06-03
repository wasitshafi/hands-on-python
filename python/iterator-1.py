# you can assume that myCustomRange has 2 data members as limit, start and a local variale currVal ( we can simply return and increment start so to avoid using a currVal variable )
# for more info read : https://www.geeksforgeeks.org/iterators-in-python/

class myCustomRange:
    def __init__(self, n): # This will be called on once
        self.limit = n     
    def __iter__(self):    # This will also be called once  and mostly used to initialize some thing
        self.start = 0
        return self
    def __next__(self):
        currVal = self.start
        if currVal > self.limit:
            raise StopIteration
        self.start = self.start + 1 
        return  currVal

for i in myCustomRange(50):
    print (i, end = "  ")
