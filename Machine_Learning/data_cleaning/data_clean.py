import pandas as pd
import numpy as np

# load the data set
data = pd.read_csv('data_sets/Titanic-Dataset.csv')
data.head()

# check duplicates
duplicates = data.duplicated()
#print(duplicates)

# check data info
#datInfo = data.info()
#print("Data Info : ", datInfo)

# categorical columns
cat_col = [col for col in data.columns if data[col].dtype == "object"]
#print("Categorical columns : ", cat_col)

# numerical columns
num_col = [col for col in data.columns if data[col].dtype != "object"]
#print("Numerical columns : ", num_col)

# check total number of unique values in the categorical columns
unique_values = data[cat_col].nunique()
#print("Number of unique values : ", unique_values)

# print 50 unique tickets
tickets = data['Ticket'].unique()[:50]
#print(tickets)

# drop the name and ticket columns
data1 = data.drop(columns=['Name', 'Ticket'])
data1 = data1.shape
#print("After dropped name and ticket : \n", data1)

data2 = round((data.isnull().sum()/data.shape[0])*100,2)
#print("After value missing : \n", data2)

data3 = data.drop(columns='Cabin')
data3.dropna(subset=['Embarked'], axis=0, inplace=True)
data3 = data3.shape
print("after handling missing data : \n", data3)

