import numpy as np


def f(xx):
    z = (xx - np.e) ** 3
    return z


a, b = 0, 4
n = 0
while np.abs(a - b) > 10 ** -6:
    n += 1
    if n > 10 ** 4:
        break
    m = 0.5 * (a + b)
    if f(a) * f(m) > 0:
        a = m
    else:
        b = m
m = 0.5 * (a + b)
print('Total steps=', n)
print('Numerical solution=', m)
