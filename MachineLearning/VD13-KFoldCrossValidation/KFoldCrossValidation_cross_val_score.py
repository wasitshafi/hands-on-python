#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
from sklearn.model_selection import KFold
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# In[2]:

digits = load_digits()
X = digits.data
Y = digits.target

#print(X)
#print(Y)

#kf = KFold(n_splits = 10)
kf = KFold() # by default n_splits = 5

model = DecisionTreeClassifier()
sum = 0.0
for train_index, test_index in kf.split(X):
    x_train, x_test, y_train, y_test = digits.data[train_index], digits.data[test_index], digits.target[train_index], digits.target[test_index]

    # Let we use use DecisionTreeClassifier here
    model.fit(x_train, y_train)

    score = model.score(x_test, y_test)
    sum += score
    print('model.score(x_test, y_test) : ', score)
print("average score : ", sum/5)

#CTM: we can use different models (logistic regression,random forest support vector machines etc) and compare their average score, so to choose the model which will fit best for our use_case

#CTM : we can use directly 'cross_val_score' to get the score for different models'

# In[4]:

scores = cross_val_score(DecisionTreeClassifier(), digits.data, digits.target)
print('cross_val_score(DecisionTreeClassifier(), digits.data, digits.target) :', scores)
print('scores.mean() :', scores.mean())

scores = cross_val_score(SVC(), digits.data, digits.target)
print('\ncross_val_score(SVC(), digits.data, digits.target) :', scores)
print('scores.mean() :', scores.mean())

scores = cross_val_score(RandomForestClassifier() , digits.data, digits.target)
print('\ncross_val_score(RandomForestClassifier(), digits.data, digits.target) :', scores)
print('scores.mean() :', scores.mean())

# In[ ]:
