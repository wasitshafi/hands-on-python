#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from sklearn import linear_model


# In[36]:


FILE_NAME = 'homeprice.csv'
df = pd.read_csv(FILE_NAME)
print(df)


# In[41]:


# here we noticed one bedroom cell contains NaN, so we have to clean the data first
# we can remove that entire row or simpy put the mean of bedrooms

mean = df.bedroom.mean()
df.bedroom.fillna(mean, inplace= True) # fillna() will fill the value only on cells where it contains NaN
print(df)


# In[ ]:


linear_regression_model = linear_model.LinearRegression()
linear_regression_model.fit(df[['area', 'bedroom', 'age']], df.price) # miltiple linear regression
print('coefficient : ', linear_regression_model.coef_)
print('intercept   : ', linear_regression_model.intercept_)
# predicting home price
area = 3000  # features 
bedroom = 3  # features
age = 10     # features

print('\n\nlinear_regression_model.predict([[3000, 3, 40]]) : ', linear_regression_model.predict([[3000, 3, 10]])) # area, bedroom, age

# we know y = m1x1 + m2x2 + m3x3 + c
m1 = linear_regression_model.coef_[0]
m2 = linear_regression_model.coef_[1]
m3 = linear_regression_model.coef_[2]
c = linear_regression_model.intercept_
print('y = m1x1 + m2x2 + m3x3 + c : ', m1 * area + m2 * bedroom + m3 * age + c)

