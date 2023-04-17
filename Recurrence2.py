#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:12:13 2023

@author: mohammadaminbasiri
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.special import factorial
from matplotlib.ticker import MaxNLocator


def Prob(n,j):
    First = factorial(n)/(factorial(j)*factorial(n-j))
    return First*((1/n)**j)*((1-(1/n))**(n-j))

N = 100
  
A = np.zeros(shape=[1,N+1],dtype=float)        
A[0,1] = 1
A[0,2] = 2
    
for i in range(3,N+1):
    G = 1
    for j in range(2,i):         
        G = G + A[0,j] * Prob(i,j)
    D = 1 - Prob(i,0) - Prob(i,i)  
    A[0,i] = G/D
            
L = A[0,2:]
    
n=[]
for i in range(len(L)):
    n.append(i+2)
    print("L[{}] = {}".format(i+2,L[i]))


fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.plot(n[1:], L[1:], color='blue', linewidth=3)
ax.set_title('L(n)', fontweight="bold", fontsize=24)
ax.set_xlabel('n', fontweight="bold", fontsize=24)
ax.set_ylabel('L(n)', fontweight="bold", fontsize=24)
#ax.set_ylim(bottom=0)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlim(left=0)
ax.grid(True)
#plt.yscale("log")
plt.show()

