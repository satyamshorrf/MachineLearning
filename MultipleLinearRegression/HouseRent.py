import pandas as pd
import numpy as np



#### LOAD DATA ####
print('-'*30);print("IMPORTING DATA");print('-'*30);
data = pd.read_csv('houses_to_rent.csv', sep = ',')
print(data.head())
data = data [['city','rooms','bathroom', 'parking spaces','fire insurance','furniture','rent amount']]

print(data.head())


#### PROCESS DATA  ######
data['rent amount'] = data['rent amount'].map(lambda i: int(i[2:].replace(',','')))
data['fire insurance'] = data['fire insurance'].map(lambda i: int(i[2:].replace(',','')))
data['furniture'] = pd.factorize(data['furniture'])[0]
print(data.head())

print('-'*30);print("CHECKING NULL DATA");print('-'*30);
print(data.isnull().sum())
#data = data.dropna()
print('-'*30);print("HEAD");print('-'*30);
print(data.head())

#### SPLT DATA ####
print('-'*30);print(" SPLIT DATA ");print('-'*30);
x = data.drop(['rent amount'], axis=1)
y = data['rent amount']
print('X', x.shape)
print('Y', y.shape)





# Shuffle the data
shuffled_data = data.sample(frac=1, random_state=10).reset_index(drop=True)

# Calculate the split index
train_size = int(0.8 * len(shuffled_data))

# Split the data
train_data = shuffled_data[:train_size]
test_data = shuffled_data[train_size:]

xTrain = train_data.drop(['rent amount'], axis=1)
yTrain = train_data['rent amount']
xTest = test_data.drop(['rent amount'], axis=1)
yTest = test_data['rent amount']


print('XTrain',xTrain.shape)
print('XTest',xTest.shape)

































