import pandas as pd
names=["shyam","satya","manikanta","pavan","devi","satya","priyanka"]
ages=[19,19,19,19,18,18,18]
salaries=[100000,200000,300000,120000,150000,100000,200000]
employies_data={"names":names,"ages":ages,"salaries":salaries}
employies=pd.DataFrame(employies_data)
employies.reset_index(inplace=True)
employies.set_index(["ages"],inplace=True)
k=[employies[["salaries"]].groupby("ages").mean(),employies[["salaries"]].groupby("ages").median()]
print(k)
