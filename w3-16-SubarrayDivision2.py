#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    seg_count = 0
    for i in range(len(s) - m + 1):
        seg = s[i:i + m]
        if sum(seg) == d:
            seg_count += 1
    return seg_count    
    
    
 #Iterate through  array, look at 
# slice of  array starting at  current index 
# ending at the current index plus m. 
#If sum of this slice is equal to d, 
#increment counter. 
##Finally return counter.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result = birthday(s, d, m)
    fptr.write(str(result) + '\n')
    fptr.close()
