import numpy as np

def f(x):
    return np.sin(x)

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        sum += f(a + i * h)
    return h * sum

def romberg_integration(a, b, max_order):
    R = np.zeros((max_order, max_order))
    for i in range(max_order):
        n = 2**i
        R[i, 0] = trapezoidal_rule(a, b, n)
        for k in range(1, i+1):
            R[i, k] = (4**k * R[i, k-1] - R[i-1, k-1]) / (4**k - 1)
    return R

R = romberg_integration(0, np.pi, 4)
print(R)