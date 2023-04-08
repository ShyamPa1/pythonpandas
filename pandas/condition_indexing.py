import pandas as pd
sales=pd.read_excel("C:\\Users\\DELL\\Downloads\\sales.xlsx")
#gives the bollean value
print(sales[["Profit"]]>0)
#dataframes
print(sales[sales["Profit"]>0])
#multiple conditions
s=sales[(sales["Sales"]>250000)&(sales["Market"].isin(["Europe","LATAM"]))]
print(s)