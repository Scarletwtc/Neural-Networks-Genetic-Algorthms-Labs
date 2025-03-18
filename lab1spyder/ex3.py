import numpy as np
import matplotlib.pyplot as plt

grade = 4.45
print(np.ceil(grade))
print(np.floor(grade))

b=np.array([1,2,3,4,5,6,7,8])
print(b)
print(np.size(b))

print()

#what does this do?

print(b[4])

print(b[0:4])

print()

print(b[-2])

print(b[:3])

print(b[3:])

print(b[::-1])

#if we have -1 on stop side it goes in reverse b[start:end]


print(b[3::])
#happy? yh but this way u dnt eat too its bok

