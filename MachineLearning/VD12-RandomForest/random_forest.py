#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier


# In[5]:


digits = load_digits()
#print(dir(digits))

X = digits.data
Y = digits.target

#print(X)
#print(Y)
#print(digits.feature_names)

x_train, x_test,y_train, y_test = train_test_split(X, Y, test_size=.2)

model = RandomForestClassifier()
model.fit(x_train, y_train)
model.score(x_test, y_test)


# In[ ]:




