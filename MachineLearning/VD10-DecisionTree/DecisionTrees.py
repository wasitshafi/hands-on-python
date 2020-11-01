#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder # for one hot encoding
from sklearn.tree import DecisionTreeClassifier


# In[51]:


FILE_NAME = 'salaries.csv'
df = pd.read_csv(FILE_NAME)
#print(df)

# Divided into target variable and independent variable
inputs = df.drop('salary_more_then_100k', axis = 'columns') # X
targets = df['salary_more_then_100k']      # Y

#print(inputs)
#print(targets)

le_company = LabelEncoder() # creating objects
le_job = LabelEncoder()
le_degree = LabelEncoder()

# adding new columns to df
inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_company.fit_transform(inputs['job'])
inputs['degree_n'] = le_company.fit_transform(inputs['degree'])
#print(inputs)

# now we don't need column with nominal variables, so drop them
inputs = inputs.drop(['company', 'job', 'degree'], axis='columns')

#print(inputs)
#print(targets)
# now we have of X data

x_train, x_test, y_train, y_test = train_test_split(inputs, target, test_size = .25)
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

print('model.score(x_test, y_test) : ', model.score(x_test, y_test))
#print(x_test)
y_predicted = model.predict(x_test)
# company 0,1,2 ==abc pharma, facebook, google
# job 0, 1, 2 == business manager, computer programmer, sales executives
# degree 0 ,1 == bachelors, masters
print('x_test      : \n', x_test)
# y_predicted 0, 1 === not salary_more_then_100k, salary_more_then_100k 
print('\n\ny_predicted : ', y_predicted)

