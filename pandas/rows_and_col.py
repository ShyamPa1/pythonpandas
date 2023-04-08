import pandas as pd
data = pd.read_csv("C:\\Users\\DELL\\Downloads\\shyam\\annual.csv.csv",index_col=[0,2])
print(data.index.names)
# del data.index.name

print(data)