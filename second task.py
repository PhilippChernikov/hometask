
import math

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
