#!/bin/python3

import math
import os
import random
import re
import sys


def closestNumbers(arr):
    arr.sort()
    
    a = []  #answer
    m = abs(arr[1]-arr[0]) #minDistance start
    
    for i in range(len(arr)):
      
        if abs(arr[i]-arr[i-1])>m: #if greater then min
            continue
            
        if abs(arr[i]-arr[i-1])<m: #if smaller then min
            m = abs(arr[i]-arr[i-1])  #set new min
            a = []                  #empty old ans  
        a.append(arr[i-1])   #append to new ans
        a.append(arr[i])     
        
    return a

    
   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
