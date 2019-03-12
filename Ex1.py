# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:39:02 2019

@author: user
"""

import numpy as np
import random as rd

A=np.arange(0,10)
i=9

for y in range(0,9):
    x=rd.randint(0,i)
    b=A[x]
    c=A[i]
    A[x]=c
    A[i]=b
    i -=1
    
print(A)