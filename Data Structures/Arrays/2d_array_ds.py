#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    # It is know that the arris a 6x6 matrix
    # Hourglasses are centered along any of the elements not in the edges of the matrix
    
    max_sum = -9 * 6 * 6 # Minimmum possible sum

    for i in range(1, 5):
        for j in range(1, 5):
            top_part = sum([arr[i - 1][k] for k in range(j - 1, j + 2)])
            bottom_part = sum([arr[i + 1][k] for k in range(j - 1, j + 2)])
            hourglass_sum = top_part + bottom_part + arr[i][j]
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum
    
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()