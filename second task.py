Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math

iterations = 20

def my_cosh(x):
    x_pow = 1
    multiplier = 1
    partial_sum = x
    for n in range(1, iterations):
        x_pow *= x**2  
        multiplier *= 1 / (2*n-1) / (2*n) 
        partial_sum += x_pow * multiplier
    return partial_sum

print(my_cosh(0.125))
print(math.cosh(0.125))
