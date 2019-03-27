#!/bin/python3

import math
import os
import random
import re
import sys

# TODO: Finish implementing the formingMagicSuare function

def formingMagicSquare(s):
    repeats = {}
    seen = {}
    for row in range(3):
        for col in range(3):
            if s[row][col] not in seen:
                seen[s[row][col]] = [(col, row)]
            else:
                repeats[s[row][col]] = [(col, row)] + seen[s[row][col]]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
