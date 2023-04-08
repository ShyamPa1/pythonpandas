import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
#row slicing
df_2=df[0::2]
print(df_2.head(20))
#colmuns slicing
df_3=df[["X","Y"]]
print(df_3)