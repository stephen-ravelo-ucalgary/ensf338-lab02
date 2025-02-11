import timeit
import cProfile

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    #third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

if __name__ == "__main__":
    with cProfile.Profile() as pr:
        test_function()
        third_function()
    pr.print_stats()

#   1. What is a profiler, and what does it do?
#       A profiler is a tool that measures the performance of specific parts of a program
#       by tracking execution time and function calls by looking at a profile.
#       A profile is a set of statistics which give this information and can be generated
#       using cProfile or profile.

#   2. How does profiling differ from benchmarking?
#       Profiling differs from benchmarking, as profiling focuses on identifying where most of
#       the execution time is spent in the code, whereas benchmarking measures the time taken
#       to execute a specific piece of code (typically through the use of timeit). Profiling
#       provides detailed stats on how often and how long various parts of the program 
#       executed through the generation of a execution profile for a program.

#   3. Use a profiler to measure execution time of the program (skip function definitions)
#       Code found above^^

#   4. Discuss a sample output. Where does the execution time go?
#       Sample output;
#          70 function calls (25 primitive calls) in 2.833 seconds

#           Ordered by: standard name

#          ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#               1    0.000    0.000    0.000    0.000 cProfile.py:118(__exit__)
#               1    0.000    0.000    0.000    0.000 ex3.py:11(test_function)
#               1    0.000    0.000    2.833    2.833 ex3.py:17(third_function)
#               1    2.833    2.833    2.833    2.833 ex3.py:19(<listcomp>)
#           55/10    0.000    0.000    0.000    0.000 ex3.py:4(sub_function)
#              10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#               1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#           According to the sample output, the execution time is largely used on third_function(),
#           as the output states ex3.py:19(<listcomp>) is the line where most of the time is used.
#           The line in question is return [i**2 for i in range(100000000)], which is where the execution time goes.
#           As the cumtime of 2.833 is entirely due to that line. Another point that can be gathered from the sample
#           output is that sub_function() is called 55 times, with 10 of those being non-recursive calls.
#           third_function() and test_function() are only called once.
