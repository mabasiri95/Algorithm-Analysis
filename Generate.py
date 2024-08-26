#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:12:13 2023

@author: mohammadaminbasiri
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from random import random

X = []
Y = []
count = 0

N = 10**3

for i in range(N):
    x = random()
    y = random()
    X.append(x)
    Y.append(y)
    if (x-0.5)**2 + (y-0.5)**2 < 0.25:
        count = count + 1

print("This is the estimate of pi/4 with N = {}\n".format(N),count/N)
print("This is the real value of pi/4\n",np.pi/4)

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
ax.scatter(X, Y, color='red', linewidth=1)
ax.scatter(0.5, 0.5, color='blue', linewidth=550)
ax.set_title('Random Dots', fontweight="bold", fontsize=24)
ax.set_xlabel('X', fontweight="bold", fontsize=24)
ax.set_ylabel('Y', fontweight="bold", fontsize=24)
ax.set_ylim(bottom=0, top = 1)
ax.set_xlim(left=0, right=1)
ax.grid(True)
#plt.yscale("log")
plt.show()



a = [1000, 10000, 100000, 1000000]
b = [0.773, 0.7904, 0.7871, 0.785017]
c = [np.pi/4, np.pi/4, np.pi/4, np.pi/4] 

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
ax.plot(a, b, color='blue', linewidth=3)
ax.plot(a, c, '--', color='red', linewidth=1)
ax.set_title('estimate', fontweight="bold", fontsize=24)
ax.set_xlabel('N', fontweight="bold", fontsize=24)
ax.set_ylabel('estimate', fontweight="bold", fontsize=24)
ax.grid(True)
plt.xscale("log")
plt.show()