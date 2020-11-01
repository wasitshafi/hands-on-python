#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline


# In[2]:


df = pd.read_csv('spam.csv')
#print(df)

X = df.Message
le = LabelEncoder()
Y = le.fit_transform(df['Category']) # 0 for ham , 1 for spam

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = .2)

v = CountVectorizer()
#print(x_train)
x_train_count = v.fit_transform(x_train.values)
#print(x_train_count.toarray()[:5])

model = MultinomialNB()
model.fit(x_train_count, y_train)

#print('model.score(x_train_count, y_train) :',model.score(x_train_count, y_train))

x_test_count = v.transform(x_test)
#print(x_test_count) # we can't directly give raw data to model to predict, we need to first transform it
y_predicted = model.predict(x_test_count)
print(y_predicted)


# In[9]:


# The overhead of transforming x_train/x_test each using countvectorizer can be reduced using sklean pipline method
model = Pipeline([('vectorizer', CountVectorizer()), ('nb', MultinomialNB())])

model.fit(x_train, y_train) # passing directly x_train (email body text)
print('model.score(x_test, y_test) : ', model.score(x_test, y_test))

