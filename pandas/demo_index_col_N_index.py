import pandas as pd

FILE_NAME = 'file1.csv'
df = pd.read_csv(FILE_NAME) # by defaul for accessing row, index [0, n-1] will be added
df1 = pd.read_csv(FILE_NAME, index_col=0) # setting 1 column as index
df2 = pd.read_csv(FILE_NAME, index_col=1) # setting 2 column as index

print('df : \n', df)
print('\n\ndf1 : \n', df1)
print('\n\ndf2 : \n', df2)

print('\ndf.loc[2] : \n', df.loc[2])
print('\ndf1.loc[102] : \n', df1.loc[102])
print('\ndf2.loc[\'Amir Khan\'] : \n', df2.loc['Amir Khan'])

# Saving with index
df.to_csv('withindex.csv')

# Saving without index
df.to_csv('withoutindex.csv', index=False)