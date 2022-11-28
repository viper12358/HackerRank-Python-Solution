#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s start of sam house
#  2. INTEGER t end of sam house
#  3. INTEGER a location of apple tree
#  4. INTEGER b location of orange tree
#  5. INTEGER_ARRAY apples, len is the # of apples, each index is
#  the throwing distance, neg = left, pos = right
#  6. INTEGER_ARRAY oranges, en is the # of oranges, each index is
#  the throwing distance, neg = left, pos = right


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    applesCount = 0
    orangesCount = 0
    
    for i in range(len(apples)):
        if (apples[i] +a  <= t) and (apples[i] + a >= s):
            applesCount+=1
            
    for i in range(len(oranges)):
        if (oranges[i] + b <= t) and (oranges[i] + b >= s):
            orangesCount+=1
    
    print(applesCount)
    print(orangesCount)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
