import random
import numpy as np
from numba import jit
import matplotlib.pyplot as plt

def latticeformer(L):
    isingspins=np.array([(-1)**(random.choice((1,2,3,4,5,6,8,10))) for i in range(0,L*L)])
    lattice=isingspins.reshape(L,L)
    return lattice


def energy_calculator(lattice,J,L):
    lattice1=lattice
    lattice2=np.concatenate((lattice1,lattice,lattice1))
    lattice3=np.concatenate((lattice2.T,lattice2.T,lattice2.T))
    lattice3=lattice3.T
    E=0
    for i in range (L,L+L-1):
        for j in range (L,L+L-1):
            E=E+lattice[i][j]*(lattice[i+1][j]+lattice[i][j+1]+lattice[i][j-1]+lattice[i-1][j])
    print(E)
    


size=int(input("Enter square lattice size="))
J=input("Enter value of exchange constant J=")
lattice=latticeformer(size)
energy_calculator(lattice,J,size)




