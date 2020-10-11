#! /usr/bin/env python3
import numpy as np
import pandas as pd

############## Series ##############
# Series is like a 1-D Array

ser = pd.Series(np.random.rand(10)) # 10 random numbers
print('\nser : \n', ser)
print('type(ser)' , type(ser))

############## DataFrame ##############
# DataFrame is like a 2-D Array
df = pd.DataFrame(np.random.rand(100, 5)) # 10 random numbers
print('\n\nser : \n', df)
print('\ntype(ser)' , type(df))
print('\ndf.describe() \n', df.describe())
print('\ndf.shape() \n', df.shape)
print('\ndf.info() \n', df.info())


#dfc = df # it will be refrence to df
dfc = df.copy() # to create a copy of data frame
print('\n\ndfc', dfc)

############## Subset of DataFrame ##############
print('\ndf.loc[[1, 2, 3, 4, 5, 6, 9], [2, 3, 4]]\n', df.loc[[1, 2, 3, 4, 5, 6, 9], [2, 3, 4]]) # some row and columns

print('\ndf.loc[:, [2, 3, 4]]\n', df.loc[:, [2, 3, 4]]) # all rows some columns
print('\ndf.loc[[5, 14, 2, 10], :]\n', df.loc[[5, 14, 2, 10], :]) # all columns some rows

############## Queries ##############
print('\ndf.loc[df[0] > .9]\n', df.loc[df[0] > .9]) # all the rows whose column '0' has value > .9
print('\ndf.loc[(df[0] > .9) & (df[3] > .8)]\n', df.loc[(df[0] > .9) & (df[3] > .8)])

############## Selection ##############
print('\ndf.loc[3:5]\n', df.loc[3:5]) # row no 3 to 5
print('\ndf.loc[:5]\n', df.loc[:5])  # first 5 rows
print('\ndf.loc[-5:]\n', df.loc[-5:]) # last 5 rows
print('\ndf.loc[-5:]\n', df.loc[-5:]) # last 5 rows
print('\ndf.loc[:, [3]]\n', df.loc[:, [3]]) # all rows of cloumn 3
print('\ndf.loc[-5:]\n', df.loc[[3], :]) # all columns of row 3

