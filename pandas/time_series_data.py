import pandas as pd
import  matplotlib.pyplot as plt
#parse_dates attribute used to convert the string formet to date and time formet
weat=pd.read_csv("C:\\Users\\DELL\\Downloads\\weather_data.csv",parse_dates=["Date_Time"])
print(weat.head())
weat=pd.read_csv("C:\\Users\\DELL\\Downloads\\weather_data.csv",parse_dates=True,index_col="Date_Time")
print(weat.head())
weat.index.name=None
print(weat.head())
#slicing the data using date and time
print()
slic=weat.loc["October 1,2010"]
print(slic.head())
slic=weat.loc["2010-09-12 09:00:00":"2010-10-1 22:00:00"]
print(slic)
draw=weat.loc["2010-09-12 ":"2010-10-1 "]
print(draw)
#draw a line graph of temperature
draw["Temperature"].plot(kind="line")
plt.show()