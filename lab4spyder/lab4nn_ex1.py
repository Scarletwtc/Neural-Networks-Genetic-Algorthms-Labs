# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 12:20:55 2025

@author: Andra
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([ [1], [0], [2]])
# np.concatenate((var1,var2), axis...)

x = np.concatenate((x, np.ones([len(x), 1])), axis = 1)
T = np.array([[0], [2], [2]])

# we only need 2 weights here (w1 and w2)? w1 has to do with x and w2 has to do with the bias

w = np.array([ [1], [2]]) 

# learning rate
alpha = .1

#we had 2 approaches: one with while loop and one with for loop
# for while we wanted the alg to run until we reach the global error to be 0
# for for we have range, and then it runs either n*E times or 
# we also had an epsilon defined and we used this eps as a treshold in a matter of if we get a value smaller than this treshold  then we consider this approx of the tresh good enoigh to break out of the loop
 
maxE= 30
eps = 10**(-3) # 1e-3

for i in range (maxE):
    #Define Y = x*w
    Y = np.matmul(x,w)
    # Defining E = T - Y
    E = T - Y
    # calc derivative of the weight: dw 
    dw = alpha * x * E
    print ('dw=', dw)
    dw = np.sum(dw, axis = 0)
    print ('dw=', dw)
    w = w + dw
    
    eGlobal = 0.5*np.sum(E**2)
    print ('Global error:', eGlobal)
    
    if eGlobal < eps:
        break
    
print ("========================================================")
print ('w= ', w)

plt.close('all')
plt.plot(x[:,0], T, 'og')
plt.plot(x[:,0], Y, 'd-r')
plt.grid('on')    
    
    
    
    
    
    
    