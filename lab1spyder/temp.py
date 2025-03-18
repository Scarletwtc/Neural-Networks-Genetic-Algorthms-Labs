import numpy as np
import matplotlib.pyplot as plt

t= np.arange(0,2*np.pi+1, 0.1)

plt.close('all')
plt.figure('My first plot', facecolor='pink')

plt.subplot(2,1,1)
plt.title("Sine Fuction")
f1=np.sin(t)
plt.plot(t, f1, 'r')

plt.subplot(2,1,2)
plt.title("Cosine Fuction")
f2=np.cos(t)
plt.plot(t, f2, 'b')
plt.grid('on')

plt.figure('Circle', facecolor='red')
plt.axis('equal')
plt.plot(f1,f2) #circle sin & cos

