#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
#from sklearn import linear_model # alternate
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[4]:


FILE_NAME = 'carprices.csv'
df = pd.read_csv(FILE_NAME)
#print(df)

model = LinearRegression()
"""
# Training model on whole dataset
Y = df['Sell Price($)']
#df = df.drop(['Sell Price($)'], axis="columns")
#print(Y)
model.fit(df[["Mileage", "Age(yrs)"]], Y)
estimation = model.predict([[69000, 6]])
print('model.predict([[69000, 6]]', estimation)
print('score ',model.score(df[["Mileage", "Age(yrs)"]], Y))
"""
X = df[['Mileage', "Age(yrs)"]]
Y = df['Sell Price($)']
#print(X)
#print(Y)

# it not like first 80% data will be selected for training
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)#80% training data, 20% testing data, but that will be random each time
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state = 10)#80% training data, each time same sample will be used for training and testing
"""
print('len(x_train)', len(x_train))
print('x_train')

print(len(x_train)', len(x_train))
print(x_train)
print('y_train')
print(y_train)

print('x_test')
print(x_test)
print('y_test')
print(y_test)
"""


model.fit(x_train, y_train) # its better to use some part for trainging instead of use all the data for training pusposes
estimation = model.predict([[69000, 6]])
print('model.predict([[69000, 6]]', estimation)
print('score ',model.score(df[["Mileage", "Age(yrs)"]], Y))


# In[ ]:




