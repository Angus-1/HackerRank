#!/bin/python3

import math
import os
import random
import re
import sys

#1,2,3,4,5,10
#two subarrays below form trianlges
#2,3,4 
#3,4,5
#Choose the one with the longest maximum side 
#if none exists return -1

def maximumPerimeterTriangle(s):
   s = sorted(sticks) 
   b = [-1] 
                  
   for i in range(len(s)):
    a = s[i : i+2]              #slice array in indexes of 3 and assign to a
    if(s[i] + s[i+1] > s[i+2]): #check triangle condition
        return a                #get subarray with those elements, 
                                #since sorted, a will be returned once we have largest possible triangle
    return (b)                  #no triangle exist condition
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
