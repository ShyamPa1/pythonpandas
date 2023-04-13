import numpy as np
a=np.random.randint(9,size=(3,3))
b=np.random.randint(9,size=(3,3))
boolean=a>4
c=np.zeros(shape=(3,3),dtype=int)
c[boolean]=a[boolean]*b[boolean]
print(a)
print(b)
print(c)