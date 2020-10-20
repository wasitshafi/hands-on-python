#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn import linear_model


# In[2]:


file_name = 'homeprice.csv'
df = pd.read_csv(file_name)
print(df)
model = linear_model.LinearRegression() # Creating Object
model.fit(df[["area"]], df['price'])    # Traning model, after this step we can print directly predict function

area_size = int(input("Enter area size : "))
estimated_price = model.predict([[area_size]])
print('Estimated Price :', estimated_price)


# In[ ]:


# Creating and Reading  a pickle file
import pickle
print('pickle')
# Create a pickle
pickle_file_name = 'linear_model_pickle.plk' # or
pickle_file_name = 'linear_model_pickle'

# Writing Pickle Model
# Method 1
f = open(pickle_file_name, 'wb')
pickle.dump(model, f)
"""
# Method 2
with open(pickle_name, 'wb') as f: # We can also share that pickle file to some other popple wherepickle.dumb(model, f)
    pickle.dump(model, f) # (object to save in pickle, file object)
"""

# Reading Pickle Model
# Method 1
f = open(pickle_file_name, 'rb')
p = pickle.load(f)
"""
# Method 2
with open(pickle_file_name, 'rb') as f:
    p = pickle.load(f)
"""

area_size = int(input("Enter area size : "))
estimated_price = p.predict([[area_size]])
print('Estimated Price :', estimated_price)


# In[5]:


# using joblib (both pickle and joblib do the same thing, but if we are having numpy arrrays, then joblib will do the procession in less time)
import joblib

joblib_file_name = 'linear_model_pickle.joblib'#  or 
joblib_file_name = 'linear_model_pickle' 
# With joblib we can directly save and load files without creating a file object first
joblib.dump(model, joblib_file_name) # model saved

j = joblib.load(joblib_file_name)
area_size = int(input("Enter area size : "))
estimated_price = j.predict([[area_size]])
print('Estimated Price :', estimated_price)

