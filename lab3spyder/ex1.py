# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 14:07:42 2025

@author: Layla
"""

#input 
p=1
k=0

 #weight
wp = 1
wk = 1
 
 #Bias and target
 
b=1 #not linearly dependet
T=1
 
def  Y():
    return p*wp+k*wk+ b
 
    
 
    
#Average error squared
def E2():
    return 0.5*( T - Y() )**2

# 0.5 cuz if we were to calc the differentiate of power 2 then wed get multiply with 0.5 and get the error


#part of updating wp
def dE2dwp():
    return ( T - Y() )*(-p)

#part of updating wk
def dE2dwk():
    return ( T - Y() )*(-k)

#part of updating b
def dE2db():
    return ( T - Y() )*(-1)

#Teaching rate
#.1=0.1
a = .1

for i in range (10):
    print("Epoch", i , ":" ,  Y(), E2()) #epoch 
    wp -= a*dE2dwp()
    wk -= a*dE2dwk()
    b -= a*dE2db()
    
print()    