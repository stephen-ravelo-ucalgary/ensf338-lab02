import random
import timeit
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def linear_search(arr, key):
    for index, value in enumerate(arr):
        if (value == key):
            return index
    return -1

def binary_search(arr, first, last, key):
    if (first <= last):
        mid = (first + last) // 2
        if (key == arr[mid]):
            return mid
        elif (key < arr[mid]):
            return binary_search(arr, first, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, last, key)
    return -1

def log_curve_fit(x, y):
    a_guess = 6
    b_guess = 1.5
    c_guess = 0.2

    popt, pcov = curve_fit(
        lambda t, a, b, c: a * np.log(t - c) + b, x, y,
        p0=(a_guess, b_guess, c_guess)
    )
    a = popt[0]
    b = popt[1]
    c = popt[2]

    #print(a, b, c)

    x_fitted = np.linspace(np.min(x), np.max(x), 100)
    y_fitted = a * np.log(x_fitted - c) + b

    return x_fitted, y_fitted

if __name__ == "__main__":
    linear_averages = []
    binary_averages = []

    list_lengths = [1000, 2000, 4000, 8000, 16000, 32000]

    for list_length in list_lengths:
        numbers = [x for x in range(list_length)]
        lin_time = []
        bin_time = []
        
        for i in range(1000):
            key = random.randrange(list_length)
            time = timeit.timeit(lambda: linear_search(numbers, key), number = 100)
            lin_time.append(time / 100)
            time = timeit.timeit(lambda: binary_search(numbers, 0, list_length - 1, key), number = 100)
            bin_time.append(time / 100)

        linear_average = sum(lin_time) / len(lin_time)
        linear_averages.append(linear_average)
        binary_average = sum(bin_time) / len(bin_time)
        binary_averages.append(sum(bin_time) / 1000)
        print("List length: %d\nLinear: %f\nBinary: %f\n" % (list_length, linear_average, binary_average))

    fig = plt.figure()

    slope, intercept = np.polyfit(list_lengths, linear_averages, 1)
    line_values = [slope * x + intercept for x in list_lengths]
    ax1 = fig.add_subplot(121)
    ax1.plot(list_lengths, line_values, 'r', c='b', label="Fitted line")
    ax1.scatter(list_lengths, linear_averages, c='black', label="Raw data")
    ax1.set_title(r'')
    ax1.set_ylabel('Time')
    ax1.set_xlabel('List Length')
    ax1.set_ylim(0)
    ax1.set_xlim(0)
    ax1.legend()

    x_fitted, y_fitted = log_curve_fit(list_lengths, binary_averages)
    ax2 = fig.add_subplot(122)
    ax2.plot(x_fitted, y_fitted, 'k', c='r', label="Fitted curve")
    ax2.scatter(list_lengths, binary_averages, c='black')
    ax2.set_title(r'')
    ax2.set_ylabel('Time')
    ax2.set_xlabel('List Length')
    ax2.set_ylim(0)
    ax2.set_xlim(0)
    ax2.legend()

    plt.show()