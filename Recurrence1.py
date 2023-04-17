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

N = 20
  
A = np.zeros(shape=[1,N+1],dtype=int)        
A[0,1] = 1
    
for i in range(1,N):
    Sum = 0
    for j in range(1,i+1):         
        Sum = Sum + A[0,j] * A[0,i+1-j]
        
    A[0,i+1] = Sum
            
P = A[0,1:]
    
n=[]
for i in range(len(P)):
    n.append(i+1)
    print("P[{}] = {}".format(i+1,P[i]))


fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.plot(n[1:], P[1:], color='blue', linewidth=3)
ax.set_title('P(n) for 2 <= n <= 20', fontweight="bold", fontsize=24)
ax.set_xlabel('n', fontweight="bold", fontsize=24)
ax.set_ylabel('P(n)', fontweight="bold", fontsize=24)
ax.set_ylim(bottom=0)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlim(left=2)
ax.grid(True)
#plt.yscale("log")
plt.show()








    
    







# def Parenthesizing(n, verbose=False):
#     if verbose:
#         print("Parenthesizing n=", n)
    
#     m = np.zeros(shape=[1,n+1],dtype=int)
#     if verbose:
#         print(m[0,1:])
        
#     j=1
#     m[0,j] = 1 #P(1) = 1
#     if verbose:
#         print(j, m[0,1:])
        
#     for jj in range(1,n):
#         j = jj + 1
#         if verbose:
#             print("j = ",j)
            
#         s = 0
#         nn = j
#         for kk in range(1, nn):
#             k = kk
#             if verbose: 
#                 print("m[%d]"%j,"+=", "m[%d]"%k,m[0,k], "* m[%d]"%(nn-k), m[0,nn-k])
            
#             s = s + m[0,k] * m[0,nn-k]
            
#         m[0,j] = s
#         if verbose:
#             print(j, m[0,1:])
            
#     if verbose: 
#         print("Parenthesizing(%d) = "%n,m[0,1:])
#     return m[0,1:]
    
# P = Parenthesizing(10)
# for j in range(len(P)):
#     print("P(%d) =%d"%(j+1,P[j]))