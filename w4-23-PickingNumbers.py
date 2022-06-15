#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#solution 1 (does not pass all cases misses 2)
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

#solution 2 using dict, passes all test cases   
def pickingNumbers(a):
    a.sort()
    nums = defaultdict(int)
    maxSub = 0
    for i in a:
        nums[i] += 1
    for i in range(1,100):
        maxSub = max(maxSub,nums[i] + nums[i+1])   
    return maxSub    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
