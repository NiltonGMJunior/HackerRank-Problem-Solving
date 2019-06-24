#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    positive_ratio = sum([elem > 0 for elem in arr]) / n
    negative_ratio = sum([elem < 0 for elem in arr]) / n
    zero_ratio = sum([elem == 0 for elem in arr]) / n
    print("{:.6f}\n{:.6f}\n{:.6f}".format(
        positive_ratio, negative_ratio, zero_ratio))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
