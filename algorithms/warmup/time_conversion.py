#!/bin/python3

import os
import sys

def timeConversion(s):
    hours = int(s[:2])
    isAM = s[-2:] == 'AM'
    if (hours == 12):
            return ('00' if isAM else '12') + s[2:-2]
    else:
        return str(hours + (0 if isAM else 12)).rjust(2, '0') + s[2:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
