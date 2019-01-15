#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    sum_primary = 0
    sum_secondary = 0
    
    matrix_order = len(arr) # The array is always square

    for i in range(n):
        sum_primary += arr[i][i]
        sum_secondary += arr[i][n - 1 - i]
    
    return abs(sum_primary - sum_secondary)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()