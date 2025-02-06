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
