# Uses python3
import sys
import numpy as np

# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % 10


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    def cal_fib3min(n):
        a, b = 0, 1
        while n > 0:
            yield b
            a, b = b, a + b
            n -= 1
    return list(cal_fib3min(n))[-1] %10




if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
