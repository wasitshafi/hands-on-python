from collections import Counter

dict = []
dict.append('one')
dict.append('two')
dict.append('five')
dict.append('three')
dict.append('four')
dict.append('one')
dict.append('four')
dict.append('five')
dict.append('six')
dict.append('four')
dict.append('one')

print('dict []           :', dict, end="\n\n")
counter = Counter(dict)
print('counter          :', counter, end="\n\n")

print('counter.keys()   :', counter.keys(), end="\n\n")
print('counter.values() :', counter.values(), end="\n\n")

"""
# how to print key, values
for key in counter.keys():
    print(key, dict.value(str(key))
"""