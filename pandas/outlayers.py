import pandas as pd
import matplotlib.pyplot as plt
sales=pd.read_excel("C:\\Users\\DELL\\Downloads\\sales.xlsx")

print(sales.info())
print(sales.describe())
sales[["Profit","Sales"]].plot(kind="box",subplots=True)
plt.show()