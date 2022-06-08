#!/bin/python3

import math
import os
import random
import re
import sys

#Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            return i  
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
