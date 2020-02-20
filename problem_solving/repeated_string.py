#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    length = len(s)
    num_a = 0

    # 'a' number in string
    for i in range(0, length):
        if(s[i] == "a"):
            num_a += 1
    #length is always greater than 1, so need for checking 0
    #number of "s" string in substring
    
    total_num_a = (n // length) * num_a

    #incompleted string size
    left_string = n % length

    #number of "a" in incompleted string
    for i in range(0, left_string):
        if(s[i] == "a"):
            total_num_a += 1

    return total_num_a



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

