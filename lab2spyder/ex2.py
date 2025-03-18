import numpy as np


T = np.array([0, 0, 1, 0, 1])

x = np.array([[1, 0], [2, 0], [3, 0], [0, 1], [0, 2]])

a = np.ones(len(x))

X = np.concatenate((x, a[:, np.newaxis]), axis=1)

w = np.array([1, 3, 2])

while 1:
    n = np.matmul(X,w)
    
    y= (n>=0) * 1
    
    #e = T[i] -y
    e=T -y
    print('e =' , e)
    
    #np.tile(v,no)
    # it repeats v the amount of no times
    #E = np.tile(e, (3,1))
    E = np.tile(e, (np.size(X,1),1)) #he says he reverse engineered to write less hardcoded version
    print('E =' , E)
    
    eGlobal = np.sum(np.abs(E))
    print('Global error now is...', eGlobal)

    if eGlobal ==0:
        break
    #dw =X[i] *e
    #due to matrix mut, rules, we need to use E.T
    E = E.T
    dw = X* E
    
    dw = sum(dw)
    w = w+dw
    
print('w= ' ,w)
    