#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    negCount = 0
    posCount = 0
    zeroCount = 0
    
    for i in range(len(arr)):
        if arr[i] > 0:
            posCount += 1
        elif arr[i] < 0:
            negCount += 1
        else:
            zeroCount += 1
    negPercentage = negCount/len(arr)
    posPercentage = posCount/len(arr)
    zeroPercentage = zeroCount/len(arr)
    
    print(format(posPercentage, '.6f'))
    print(format(negPercentage, '.6f'))
    print(format(zeroPercentage, '.6f'))

            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
