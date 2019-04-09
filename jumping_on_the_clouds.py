#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    #assumed it is always possible to win the game(cases are suitable)
    #so n=6 c=[0,1,1,...0] case ignored. Because in a case like this,
    #you cannot end your jumps
    #if two 1s came in order, then the algorithm not works.
    i = 0
    jumpCount = 0
    n = len(c)
    while(i < n-2):
        if(c[i+2] == 0):
            i += 2
            jumpCount += 1
        else:
            if(c[i+1] == 0):
                i += 1
                jumpCount += 1
    if(i == n-2):
        jumpCount += 1
    return jumpCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

