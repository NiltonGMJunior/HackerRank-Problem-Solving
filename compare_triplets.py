#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    alice_points = len(list(filter(lambda ratings: ratings[0] > ratings[1], zip(a, b))))
    bob_points = len(list(filter(lambda ratings: ratings[0] < ratings[1], zip(a, b))))
    return alice_points, bob_points

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
