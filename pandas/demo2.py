#! /usr/bin/env python3
import numpy as np
import pandas as pd

############## Dictionary ##############
dict1 = {
  "name": ['wasit', 'hamid', 'zain', 'shivam', 'arjun'],
  "city": ['Srinagar', 'Bihar', 'UP', 'Delhi', 'New Delhi'],
  "sgpa": ['7.5', '8', '8.5', '9', '9.5']
}

############## Creating DataFrame ##############
df = pd.DataFrame(dict1)
print('\ndf :\n', df)

############## Accessing Cell ##############
print('\n\ndf.loc[1]["city"]', df.loc[2]['city'])
print('df.iloc[2][1]', df.iloc[2][1])

############## Changing Indexes ##############

df.columns = ['NAME', 'CITY', 'SGPA']
df.index = ['one', 'two', 'three', 'four', 'five']
# Alternate
#df = df.rename(columns={'name': 'NAME', 'city': 'CITY'}, index={0: 'one', 1:'two'})
print(df)
print('\ndf :\n', df)

############## Accessing Cell Again ##############
print('\n\ndf.loc[1]["city"]', df.loc['two']['CITY'])
print('df.iloc[2][1]', df.iloc[2][1])


############## Reset the index ##############
df = df.reset_index(drop=True) # drop=true will delete that new index column, else it will reset the columns but will also add new index column
############## pandas data frame to numpy array ##############
print('\n\ndf.to_numpy() : \n')
print(df.to_numpy())

############## tranpose data frame ##############
print('\n\ndf.T : \n')
print(df.T)

############## Sort by index ##############
# CTM: we are sorting here by column/row name/number not according to the values stored in the data frame
print('\ndf :\n', df)
# They are not mutator methods unless it's like df = df.sort()
print('\n\ndf.sort_index(axis=0) : \n', df.sort_index(axis=0)) # ascending order default, axis=0 for row wise sort
print('\n\ndf.sort_index(axis=0, ascending=False) : \n', df.sort_index(axis=0, ascending=False))
print('\n\ndf.sort_index(axis=1) : \n', df.sort_index(axis=1)) # axis=1 is column wise sort
print('\n\ndf.sort_index(axis=1, ascending=False) : \n', df.sort_index(axis=1, ascending=False)) # axis=1 is column wise sort
print('\ndf :\n', df)

# If inplace is set to True then actual data frame will modify using sort
print('\n\ndf.sort_index(axis=1, inplace= True) : \n', df.sort_index(axis=1, inplace= True)) # axis=1 is column wise sort
print('\ndf :\n', df)

############## Droping a row/column ##############
print('\ndf.drop(3) :\n',df.drop(3))
print('\ndf.drop(name), asix=1 :\n',df.drop('NAME', axis=1))