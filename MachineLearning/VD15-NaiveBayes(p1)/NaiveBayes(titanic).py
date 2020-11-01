#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder


# In[17]:


df = pd.read_csv("titanic.csv")
Y = df.Survived
df.drop(['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked', 'Survived'], axis = 'columns', inplace = True)

#print(df)
#print(Y)

le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

df.Age.fillna(df.Age.mean(), inplace = True)
# print (df)

x_train, x_test, y_train, y_test = train_test_split(df, Y, test_size = .2)
model = GaussianNB()
model.fit(x_train, y_train)

y_predicted = model.predict(x_test)
#print('x_test : ', x_test)
#print('y_predicted : ', y_predicted)


print('model.score(x_test, y_test) : ', model.score(x_test, y_test))
#model.predict_proba(x_test) # check probability for whole dataset
print(y_predicted[:10])   # 0 means passenger will not survive, so its corresponding probability will be high
model.predict_proba(x_test[:10]) # first 10 inputs


# In[ ]:




