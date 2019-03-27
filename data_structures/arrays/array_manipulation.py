#!/bin/python3

#   TODO:   Implement function arrayManipulation that works regardless of number of querries or length of array (n) using only Python built-in functions/modules
import math
import os
import random
import re
import sys
# import numpy as np

# I still don't fully understand the following algorithm
def arrayManipulation(n, queries):
    arr = [0] * n
    for query in queries:
        start_index = query[0]
        end_index = query[1]
        value = query[2]
        arr[start_index - 1] += value
        if end_index - 1 <= n:
            arr[end_index - 1] -= value
    max = 0
    aux = 0
    for i in arr:
        aux += i
        if aux > max:
            max = aux
    return max
'''
# The following doesn't work for very big inputs (auxiliary space limitations)
def arrayManipulation(n, queries):
    arr = [0] * n # This creates the base array of length n with all zeros

    # The fololowing loops through all the queries and performs the operations on arr
    for query in queries:
        start_index = query[0]
        end_index = query[1]
        value = query[2]
        arr_to_add = [0] * (start_index - 1) + [value] * (end_index - start_index + 1) + [0] * (n - end_index)
        arr = [a + b for a, b in zip(arr, arr_to_add)]

    return max(arr)
'''
'''
#   This could work, but HackerRank doesn't import numpy
def arrayManipulation(n, queries):
    arr = np.zeros(n)
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        temp = np.concatenate(np.zeros(a - 1), k*np.ones(b - a - 1), np.zeros(n - b))
        arr += temp
    return max(arr)
'''
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
