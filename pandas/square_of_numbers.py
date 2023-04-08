import numpy as np
import pandas as pd
inp=int(input("enter how many digits you want:"))
arr=np.arange(1,inp+1)
s=pd.Series(arr**2,index=arr)
print(s)