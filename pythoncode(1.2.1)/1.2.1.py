import numpy as np

A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])

D=((C+B)/2)
E=((B+A)/2)
F=((A+C)/2)

print("midpoint of BC is " , end=" " )
print(D)

print("midpoint of AB is " , end=" "  )
print(E)

print("midpoint of AC is " , end=" "  )
print(F)

