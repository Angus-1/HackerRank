#!/bin/python3

import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)       #sort arr
    m = abs(arr[1]-arr[0])  #min diff set to first pair 
    for i in range(1, len(arr)-1):    #iterate through
        if abs(arr[i]-arr[i+1]) < m:  #if less then curr minD replace
            m = abs(arr[i]-arr[i+1])
    return m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
