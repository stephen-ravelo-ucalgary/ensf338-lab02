# Exercise 2 Answers

### Question 1
Interpolation search works with uniformly distributed data. It approximates the portion of the array where the target can reside, which can disregard a large potion of the data leading to faster search times.
It can also adjust the starting position based on the given target, unlike binary that is fixed to the middle of the given array.
### Question 2
If the data follows a different distribution, for example, right or left skewness, it's calculation of the starting position is likely to be incorrect. This leads to more iterations of the while loop, and in the worst case, it can take n iterations to find the target which is slower than binary search and similar to linear search.
### Question 3
To make the algorithm work for a different distribution of data, it's calculation of the starting position would have to be modified.
### Question 4
Since both binary and interpolation search require sorted data, linear search is the only option for data that is unsorted and has a non-uniform distribution.
### Question 5
Linear search outperforms both binary and interpolation search in the case that the target element is the first element of the array as this would result in a time complexity of O(1). Another case is when the dataset or array is very small, where the logic behind binary and interpolation search may seem unnecessary. Lastly, the case mentioned in question 4 is also applicable.
### Question 6
One way to fix this issue is to implement a sorting algorithm within the program especially when binary search has to be used multiple times, this would result in a faster program than using linear search.
Modifying the calculation of the starting position in interpolation search to accomodate for different kinds of distributions can also alleviate some of these issues.
