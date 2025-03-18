import numpy as np

# True label vector
T = np.array([0, 0, 1, 0, 1])

# Input feature matrix (each row is a 2D point)
x = np.array([[1, 0], [2, 0], [3, 0], [0, 1], [0, 2]])

# Bias term (column of ones)
a = np.ones(len(x))

# Adding the bias column to X
X = np.concatenate((x, a[:, np.newaxis]), axis=1)

# Initial weight vector
w = np.array([1, 3, 2])

while True:
    # Global error counter
    eGlobal = 0

    for i in range(len(X)):
        n = np.sum(X[i] * w)

        # Step function
        y = 1 if n >= 0 else 0

        # Compute error
        e = T[i] - y
        eGlobal += abs(e)

        # Update weights
        dw = X[i] * e
        w = w + dw

    # Stop when all points are correctly classified
    if eGlobal == 0:
        break

print('w =', w)
