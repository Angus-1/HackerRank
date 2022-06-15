#!/bin/python3

import math
import os
import random
import re
import sys

#  A left rotation operation on an array of size n shifts each of
#  the array's elements 1 unit to the left. Given an integer, d, 
#  rotate the array that many steps left and return the result.

def rotateLeft(d, arr):
    left = arr[:d]
    right = arr[d:]
    return right + left

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
