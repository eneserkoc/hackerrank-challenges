#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    pairDict = {}

    for i in range(0, len(ar)):
        if(pairDict.get(ar[i]) is not None):
            pairDict[ar[i]] += 1
        else:
            pairDict[ar[i]] = 1
    
    print(pairDict)

    pair_number = 0
    for key, value in pairDict.items():
        if(value%2 == 0):
            pair_number += value // 2
        # no need for checking if value is zero or not,
        # because there is no key with zero value in dict
        else:
            pair_number += (value-1) // 2


    
    return pair_number
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

