#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# In[11]:


df = pd.read_csv('insurance_data.csv')
#print(df)

#print(x)
#print(y)

x_train, x_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance, train_size=.75)

model = LogisticRegression()
model.fit(x_train, y_train)
print(x_test)

print("prediction : ")
model.predict(x_test)

