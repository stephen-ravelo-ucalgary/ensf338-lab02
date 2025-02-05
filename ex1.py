'''
Answer to Questions
1. The function returns the n-th value of the Fibonacci sequence.
2. The function represents a divide-and-conquer algorithm as it uses recursion
to combine the results of each function call when it finally reaches n = 0
or n = 1, ultimately returning the n-th value of the Fibonacci sequence.
3. O(2^n)
5.
'''

import timeit
import sys
from functools import wraps
import matplotlib.pyplot as plt
import numpy as np

# Question 4
def memoize(func):      # decorator
    cache = {}          # memory, stores results for usage
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:    # add into cache if not in cache
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

    tm = timeit.timeit(lambda: fibonacci(20), number=1)
    print(tm)
    tm = timeit.timeit(lambda: orig_fibonacci(20), number=1)
    print(tm)

    no_memo = {}
    with_memo = {}

    for i in range(1, 35):
        tm = timeit.timeit(lambda: orig_fibonacci(i), number=1)
        no_memo[i] = tm

    print(no_memo)

    for i in range(1, 35):
        tm = timeit.timeit(lambda: fibonacci(i), number=1)
        with_memo[i] = tm

    no_memo = np.array(no_memo)
    print(no_memo)
    with_memo = np.array(with_memo)

    x_values = list(range(1, 35))
    x_values = np.array(x_values)
    print(x_values)
    
    plt.plot(x_values, no_memo)
    plt.show()