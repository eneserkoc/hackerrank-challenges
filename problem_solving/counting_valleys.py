#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    level = 0
    val_arr = []
    print(len(s))
    for i in range(0, len(s)):
        if(s[i] == "D"):
            val_arr.append(-1)
        else:
            val_arr.append(1)

    level = val_arr[0]

    if(level < 0):
        place_type = -1
    else:
        if(level > 0):
            place_type = 1
        else:
            place_type = 0

    valley_count = 0
    for i in range(1, len(val_arr)):
        level += val_arr[i]

        if(level > 0):
            place_type = 1
        else:
            if(level < 0):
                place_type = -1
            else:
                if(place_type == -1):
                    valley_count += 1
                place_type = 0

    return valley_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

