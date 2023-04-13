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

n = np.arange(2., 20., 1)

fig, ax = plt.subplots(figsize=(10, 7), dpi=300)
ax.plot(n, 15*n**2, color='red', label='15n^2', linewidth=3)
ax.plot(n, 8*n**3, color='blue', label='8n^3', linewidth=3)
ax.plot(n, 2**n, color='green', label='2^n', linewidth=3)
ax.plot(n, 3**n, color='orange', label='3^n', linewidth=3)
ax.plot(n, factorial((n)), color='violet', label='n!', linewidth=3)
ax.plot(n, n*np.log2(n), color='cyan', label='nlogn', linewidth=3)
ax.legend(loc='upper left', shadow=True)
# plt.savefig('accuracy.png')
ax.set_title('Comparision')
ax.set_xlabel('n, {2, ..., 20}')
ax.set_ylabel('T(n)')
ax.set_ylim(bottom=0, top = 100000)
ax.set_xlim(left=2)
ax.grid(True)
#plt.yscale("log")
plt.show()