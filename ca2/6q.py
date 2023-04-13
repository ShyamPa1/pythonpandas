import numpy as np
a=np.random.randint(0,10,size=(3,3))
b=sum(np.diagonal(a))
print(a)
print(b)