import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
c=pd.read_csv("C:\\Users\\DELL\\Downloads\\MovieAssignmentData.csv")
print(c)
print(c.info())
print(c.describe())
print(c[["Gross","budget"]])
c["Gross"]=c["Gross"]/1000000
c["budget"]=c["budget"]/1000000
print(c[["Gross","budget"]])
c["profit"]=c["Gross"]-c["budget"]
# print(c.head())
# print(c.sort_values("profit",ascending=False).head(10))
print(c.sort_values("profit",ascending=False).head(10))
c["index"]=range(0,9)
print(c.set_index("index").head(10))
