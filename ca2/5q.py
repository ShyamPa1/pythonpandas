import numpy as np
a=np.random.randint(0,10,size=(3,3))
b=np.random.randint(0,10,size=(3,3))
c=np.zeros(shape=(3,3),dtype=int)
c=a-b
print(a)
print(b)
print(c)