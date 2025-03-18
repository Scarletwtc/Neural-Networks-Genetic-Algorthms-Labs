# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 14:27:07 2025

@author: Layla
"""

#Estimate the sqrt of n 
import numpy as np
import matplotlib.pyplot as plt

n = int(input("Give me a value for n="))

def f(x):
    return x**2-n

x= np.arange(-n, n+0.1, 0.1)
z= np.zeros(len(x))

plt.close('all')
plt.plot(x, f(x))
plt.plot(x,z)
plt.grid('on')

A =0
B = n
plt.plot(A, 0, 'ok')
plt.plot(B,0,'ok')

C= (A+B)/2
eps = 10**(-14)

while 1:
    plt.plot(C, 0, '.r')
    if f(C)*f(A) < 0: #function changes sign
        B=C
    else:
        A=C
    
    if np.abs(f(C)) <eps: #why abs??ask chat 
        break
    else:
        C = (A+B)/2
        
print(C)    