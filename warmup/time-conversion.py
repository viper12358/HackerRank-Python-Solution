#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2] 
    elif s[-2:] == "AM":
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        num = int(s[:2]) + 12
        return str(num) + s[2:-2]
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
