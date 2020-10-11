#! /usr/bin/env python3
import numpy as np
import pandas as pd

############## Dictionary 1 ##############
dict1 = {
  'name' : 'wasit',
  'class' : 'MCA',
  'rollno' : '18MCA054',
  'city' : 'New Delhi'
  }
print("dict1 : ")
print(dict1)
#print('dict1 : ', dict1)
#print('dict1[\'name\'] : ', dict1["name"])

############## Dictionary 2 ##############
"""
dict2 = { # Nested Dictionary
  "18MCA001": {'name' : 'Aastha Gupta', 'city' : 'Kanpur', 'college' : 'JMI'},
  "18MCA002": {'name' : 'Abhay Rajput', 'city' : 'Delhi'},
  "18MCA003": {'name' : 'Alamdar Abbas', 'city' : 'UP'}
}

print("\ndict1 : ")
print(dict2)
print('dict2[\'18MCA002\'][\'name\'] : ', dict2['18MCA002']['name'])
print('dict2[\'18MCA002\'] : ', dict2['18MCA002'])
"""

dict2 = {
  "name": ['wasit', 'hamid', 'zain', 'shivam', 'arjun'],
  "city": ['Srinagar', 'Bihar', 'UP', 'Delhi', 'New Delhi'],
  "sgpa": ['7.5', '8', '8.5', '9', '9.5']
}

############## Creating DataFrame ##############
df1 = pd.DataFrame(dict2)
df2 = pd.DataFrame(dict2)

print('\ndf1 :\n', df1)
print('\ndf2 :\n', df2)

############## Exporting DataFrame to csv files ##############
df1.to_csv('NewData1.csv')
df2.to_csv('NewData2.csv', index=False)

############## printing subset of data frame ##############
print('\ndf1.head(3) : \n', df1.head(3)) # first n rows
print('\ndf1.tail(3) : \n',df1.tail(3)) # last n rows

############## Describing data frame ##############
print('\ndf1.describe() : \n',df1.describe())

############## Reading csv file & Updating ##############
FILE_NAME = 'NewData2.csv'
df3 = pd.read_csv(FILE_NAME)
print('\ndf3 : \n', df3)
df3['name'][0] = 'Wasit Shafi' # changed in Data Frame
df3.to_csv(FILE_NAME) # this may show an warning