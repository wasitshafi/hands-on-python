#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sn


# In[2]:


# load_digits is dataset that contain images of written image, of size 8X8(1D Arrays of 64 elements)
digits = load_digits() # creating object of load_digits()

print('\ndir(digits)')
print(dir(digits))
#print(digits)

print('\nlen(digits.data)')
print(len(digits.data)) # It contains total 1797 images

print('\ndigits.data[0]')
print(digits.data[0]) # printing first image data in the numeric form(array) (1D array of size 64)

print('\ndigits.images[0]')
print(digits.images[0]) # printing first image data in the numeric form(array) (2D array of size 8X8 representing intensity)

# Printing actual image
print('\n\ndigits.images[0]')
plt.gray()
print('digits.images[0]')
plt.matshow(digits.images[0])

print('digits.images[0]')
plt.matshow(digits.images[1])

print('digits.images[27]')
plt.matshow(digits.images[27])

# Printing all the dataset images (it will take a lot of time)
#for image in digits.images:
#    plt.matshow(image)

print('\ndigits.target[0]') # numberic form of image
print(digits.target[0])

print('\ndigits.target[1]')
print(digits.target[1])

print('\ndigits.target[27]')
print(digits.target[27])


# In[3]:


x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size = .2)# t_t_s(X, Y, test_size)

"""
print('len(x_train):', len(x_train))
print('len(y_train):', len(y_train))

print('len(x_test) :', len(x_test))
print('len(y_test) :', len(y_test))
"""

#model = LogisticRegression() # with this i was getting TOTAL NO. of ITERATIONS REACHED LIMIT.
#model = LogisticRegression(max_iter=len(x_train))
# Refer: https://stackoverflow.com/questions/52670012/convergencewarning-liblinear-failed-to-converge-increase-the-number-of-iterati


model = LogisticRegression(max_iter=100000)
model.fit(x_train, y_train)

print('\n\nmodel.score(x_test, y_test) : ',model.score(x_test, y_test))

print('model.predict(x_test)', model.predict(x_test))

# On individual images
plt.matshow(digits.images[69])
print('digits.target[69]', digits.target[69])

print('model.predict([digits.data[69]]', model.predict([digits.data[69]]))


# In[4]:


# Confusion matrix, to see where our model pridicted wrong
y_predicted = model.predict(x_test)
conf_mat = confusion_matrix(y_test, y_predicted)
print(conf_mat)


# In[13]:


# graphical representation of confusion matrix
plt.figure(figsize = (10, 7))
sn.heatmap(conf_mat, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

