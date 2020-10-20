#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn import linear_model


# In[63]:


# One Hot Encoding without using sklearn one hot encoder
FILE_NAME = 'homeprices.csv'
df = pd.read_csv(FILE_NAME)
"""
step 1 : Create dummies variable and merge them with data frame
step 2 : drop the nominal variable column
step 3 : drop any one dummy variable column because of dummy varable trap problem, which say if we one varible value can be derived from other variables then that should be avoided, although if we use that with sklear library of model will still work properly as they have already handeled that case
step 4 : save dependent variable column and drop it from df, so to provide x values
step 5 : train model
step 6 : predict
"""

dummies = pd.get_dummies(df.town) # dummies variable column 
df = pd.concat([df, dummies], axis="columns")
#print(df)
df = df.drop(['town', 'robinsville'], axis='columns')
#(1, 0) for monroe township, (0,1) for west windsor, (0, 0) for robinsville
#print(df)

model = linear_model.LinearRegression()
price = df['price'].values # to get it as in the form of array instead of data frame
# Now here our x value will be area & dummy variables, and y value will be price, so we have to drop price as well
df = df.drop(['price'], axis='columns')
#print(price)
model.fit(df, price)
x = model.predict([[2000, 1, 0]])
print('Estimated price of home in monroe township with area 2000 is :', x)
print('Model Score is : ', model.score(df, price)) # if value is 1 then it means our model is 100% perfect. here our model is 95% perfect

