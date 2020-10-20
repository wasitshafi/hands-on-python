import pickle

FILE_NAME = 'my_numbers.pkl'
numbers = ['one', 'two', 'three', 'four', 'five', 'six']

# CREATING A PICKLE
fileObj = open(FILE_NAME, 'wb') # opening in write + binary mode
pickle.dump(numbers, fileObj)   # dumping numbers list
fileObj.close()

# CREATING A PICKLE (We can use pickles to save our trained ML model)
fileObj = open(FILE_NAME, 'rb') # opening in read + binary mode
pklObj = pickle.load(fileObj)
print('pklObj       : ', pklObj)
print('type(pklObj) : ', type(pklObj))