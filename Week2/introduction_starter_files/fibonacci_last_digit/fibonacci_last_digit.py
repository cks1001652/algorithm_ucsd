# Uses python3
import sys

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

    return int(1/np.sqrt(5)*(((1+np.sqrt(5))/2)**n - ((1-np.sqrt(5))/2)**n)) %10




if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
