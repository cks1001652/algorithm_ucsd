# python3

#simple version
# def calc_fib(n):
#     if (n <= 1):
#         return n

#     return calc_fib(n - 1) + calc_fib(n - 2)


import numpy as np

def calc_fib(n):
    if n<=1:
        return n
    return int(1/np.sqrt(5)*(((1+np.sqrt(5))/2)**n - ((1-np.sqrt(5))/2)**n))


n = int(input())
print(calc_fib(n))
