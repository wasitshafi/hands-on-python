#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


# In[2]:


iris = load_iris()

print(dir(iris))
print(len(iris.data))


#for i in iris.data:
#    print(i)

# alternate
print('iris.target       :', iris.target)               # target 0, 1, 2
print('iris.target_names :', iris.target_names)   # name of iris
print('iris.feature_names:', iris.feature_names) # name of iris

print('\n\nsepal L      sepal W      petal L      petal W')
for i in iris.data:
    for j in i:
        print(j, end = "          ")
    print()


# In[3]:


x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = .2)

model = LogisticRegression(max_iter=100000)
model.fit(x_train, y_train)

print('model.score() : ', model.score(x_test, y_test))
print('x_test', x_test)
print('model.predict(x_test)', model.predict(x_test))


# In[4]:


# creating confusion matrix
y_predicted = model.predict(x_test)
conf_mat = confusion_matrix(y_test, y_predicted) # CTM: first argument is the correct value of Y
print(conf_mat)

