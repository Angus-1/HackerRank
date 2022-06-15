#!/bin/python3

import math
import os
import random
import re
import sys


def pickingNumbers(arr):
    nums = set(arr)
    most = 0  
    mostAfter=0              
    arr.sort()
    
    for a in arr:               
        if (arr.count(a) >= most) and(arr.count(a+1)>=mostAfter):
            most = arr.count(a)
            mostAfter= arr.count(a+1)     
        else: continue              
        
    return most + mostAfter    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
