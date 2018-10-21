#!/bin/python3

#   TODO:   Implement function arrayManipulation that works regardless of number of querries or length of array (n) using only Python built-in functions/modules
import math
import os
import random
import re
import sys
# import numpy as np

# Complete the arrayManipulation function below.

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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
