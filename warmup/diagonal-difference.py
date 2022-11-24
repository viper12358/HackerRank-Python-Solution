#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    leftToRight = 0
    rightToLeft = 0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                leftToRight = leftToRight + arr[i][j]
            if ((i + j) == (n - 1)):
                rightToLeft = rightToLeft + arr[i][j]
            
    result = abs(leftToRight - rightToLeft)
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()