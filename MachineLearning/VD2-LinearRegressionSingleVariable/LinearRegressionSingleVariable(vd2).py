#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[2]:


# loading data
FILENAME = 'homeprice.csv'
df = pd.read_csv(FILENAME)
print(df)


# In[3]:


# ploting a data
#%matplotlib inline

plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(df.area, df.price, color='red', marker='+')
#plt.scatter(df['area'], df['price'], color='red', marker='+')


# In[4]:


linear_regression_model = linear_model.LinearRegression() # Created Object of LinearRegression
linear_regression_model.fit(df[['area']], df.price)       # model is ready to predict now
print('perdict(35000) :', linear_regression_model.predict([[35000]]))# predcting the house price with area 400000
print('model coef_ : ', linear_regression_model.coef_)    # we know Y = MX + C, coef_ is M , and C in intercept
print('model intercept_ : ', linear_regression_model.intercept_)

# using above 2 value we can manually predice the price
m = linear_regression_model.coef_
c = linear_regression_model.intercept_
x = 35000
# In case of Linear Regression it tries to make a best-fit line
print('mx + c : ', m*x+c) # now we know how the model was able to predice the price


# In[31]:


# reading DataFrame
df_area = pd.read_csv('area.csv')
#ar = np.array(df_area['area']).reshape(-1,1) # reshape (-1,1) will make any no of rows but only 1 column 
pr = linear_regression_model.predict(df_area)
df_area['price'] = pr

#print(df_area)
df_area.to_csv('area.csv', index = 'False')

