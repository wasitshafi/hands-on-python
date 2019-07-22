for i in range(21):
    print(i, end = " ")

fruits = ["Apple", "Mango", "Orange", "Grapes"]
print ("\n")
for i in fruits:
    print (i, end = " ")

print("\n")
for i in "Ther quick brown fox jumps over to the lazy dog. Tit for tat.":
    print (i, end ="")
print( "\n\nPrinting by using __iter__() & __next__() : ")
itr = iter(fruits)
print(next(itr))
print(next(itr))
print(next(itr)) # as there are only 4 iterm if we again call 'next(itr)' it will throw StopIteration error


msg = "hello world...!"
for i in msg:
    print (i, end = "")
