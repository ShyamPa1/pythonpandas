import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
print(df.iloc[0:10:2,1:5])
print(df.loc[[4,5],["X","Y"]])
print(df.iloc[[2], [0, 1, 4]])