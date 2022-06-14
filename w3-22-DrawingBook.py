#!/bin/python3

import math
import os
import random
import re
import sys

#Given n and p , find and print the minimum number of pages that must be turned in order to arrive at page p .
def pageCount(n, p):
    return min(p//2 , n//2 - p//2)
 
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
