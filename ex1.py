'''
Answer to Questions
1.  The function returns the n-th value of the Fibonacci sequence.

2.  The function does not represent a divide and conquer algorithm because throughout
    its recursive solution calculations of the same n-th value are repeated,leading
    to duplicated calculations and excessive memory use.

3.  T(n) = T(n - 1) + T(n - 2) + 4
    Assuming T(n - 2) is approximately equal to T(n - 1)
    T(n) = 2^kT(n - k) + (2^k - 1)c
    Putting into terms of T(0) = 1, k = n
    T(n) = 2^nT(0) + (2^n - 1)c
    T(n) = (1 + c)2^n - c
    Simplifies to O(2^n)

5.  Since memoize gets rid of duplicate calculations
    T(n) = T(n) * 4
    Simplifies to O(n)
'''

import timeit
from functools import wraps
import matplotlib.pyplot as plt

# Question 4
def memoize(func):      # decorator
    cache = {}          # memory, stores results for usage
    @wraps(func)        # transfer data to actual function instead of wrapper function
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:    # add key into cache if not in cache
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

# fibonacci with memoization
@memoize
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Question 6
# fibonacci without memoization
def orig_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return orig_fibonacci(n - 1) + orig_fibonacci(n - 2)
    
if __name__ == "__main__":
    no_memo = []
    with_memo = []

    # integers 1 - 34
    for i in range(1, 35):
        tm = timeit.timeit(lambda: orig_fibonacci(i), number=1)
        no_memo.append(tm)

    # integers 1 - 34
    for i in range(1, 35):
        tm = timeit.timeit(lambda: fibonacci(i), number=1)
        with_memo.append(tm)

    x_values = list(range(1, 35))
    
    plt.plot(x_values, no_memo, label = "No Memoization")
    plt.plot(x_values, with_memo, label = "With Memoization")
    plt.xlabel("Input Value (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Fibonacci Sequence Timing")
    plt.legend()
    plt.show()
