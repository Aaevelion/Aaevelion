import random
import numpy as np
from numba import jit
import matplotlib.pyplot as plt

def latticeformer(L):
    isingspins=np.array([(-1)**(random.choice((1,2,3,4,5,6,8,10))) for i in range(0,L*L)])
    lattice=isingspins.reshape(L,L)
    return lattice



def energy_calculator(lattice,J,L,H):
    lattice1=lattice
    lattice2=np.concatenate((lattice1,lattice1,lattice1))
    lattice3=np.concatenate((lattice2.T,lattice2.T,lattice2.T))
    lattice3=lattice3.T
    sisj=0
    si=0
    for i in range (L,L+L-1):
        for j in range (L,L+L-1):
            si=si+lattice3[i][j]
            sj=lattice3[i][j]*(lattice3[i+1][j]+lattice3[i][j+1]+lattice3[i][j-1]+lattice3[i-1][j])
            sisj=sisj+sj
            
    E=-(J*sisj)-(H*si)
    print(E)
    


size=int(input("Enter square lattice size="))
H=float(input("Enter value of external magnetic field="))
J=float(input("Enter value of exchange constant J="))
lattice=latticeformer(size)
energy_calculator(lattice,J,size,H)





