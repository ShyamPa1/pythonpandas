import numpy as np
a=np.random.randint(0,10,size=(3,3))
b=np.linalg.inv(a)
print(a)
print(b)