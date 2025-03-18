# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 14:50:37 2025

@author: Layla
"""

from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron

import numpy as np
import matplotlib.pyplot as plt

X,T = load_digits(return_X_y = True)

#10**(-14) == 1e-14

model = Perceptron(tol = 1e-3, random_state = 0)
model.fit(X,T)
Y= model.predict(X)

for i in range(10):
    im= np.reshape(X[i,:], (8,8))
    plt.figure()
    plt.imshow(15-im, cmap = 'grey')
    plt.title( str(T[i])+ '-' + str(Y[i]) )
    
    #project: use  databaase that has at least 1ok iterations then decide what to do with it
    #hell use calssification to diff between flowers
    #he did travelling salesman, hard and is 10/10
    # problems similar to travelling salesman but is hard and if u solve u can integrate to bachelor
    