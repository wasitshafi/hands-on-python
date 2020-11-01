#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.svm import SVC # Support Vector Classifier


# In[21]:


iris = load_iris()
print(dir(iris))

X = iris.data
Y = iris.target

#print(X)
#print(Y)
print(iris.feature_names)

x_train, x_test,y_train, y_test = train_test_split(X, Y, test_size=.2)

model = SVC()
model.fit(x_train, y_train)
model.score(x_test, y_test)


# In[ ]:




