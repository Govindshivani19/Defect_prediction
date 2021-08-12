import pandas as pd
from pandas.plotting import scatter_matrix
dataset = pd.read_excel("/home/shivani/Desktop/dp.xlsx")
dataset.describe()
df1 = pd.DataFrame(dataset['Module'],columns=['Module'])
df1['Module'] = df1['Module'].str.replace(" ","")
print(df1.value_counts())

# dataset.describe()
# a= dataset['Module'].value_counts()
# print(a)

# Module_name=dataset.groupby('Module').size()
# print("==========================================================")
# print(Module_name)
# Priority_status=dataset.groupby('Priority').size();
# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print(Priority_status)
# Status_name=dataset.groupby('Status').size()
# print("===============================================================")
# print(Status_name)
# date_name=dataset.groupby('Date').size();
# print(date_name)
