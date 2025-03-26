# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 12:47:44 2025

@author: Andra
"""
import numpy as np
import matplotlib.pyplot as plt

import sklearn.neural_network as nn

# "predict" the XOR function

x = np.array([[0,0], [0,1], [1,0], [1,1]])

T = np.array([0,1,1,0])

# other_T = np.array([[0], [1], [1], [0]]) = just T with extra steps

# MLP Classifier = Multiple Layer Perceptron
model = nn.MLPClassifier(hidden_layer_sizes=(),
                         random_state=1,
                         max_iter=500)
model.fit(x, T)
Y = model.predict(x)

print ('T= ', T)
print ('Y= ', Y)

Z = model.score(x,T)
print ("Z= ", Z)


# test ex:
    # pls make the following math formula like n! or weite a hardcoded version of calculating the sqrt
    # or instead of giving us the XOR func for what we did today, he may give a diff function
    # we ll have a range of exercises and only a number of them will be needed to get a 10
    
    # we ll have the labboratories at our disposal and everythingg else other than the internet