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

def maximumPerimeterTriangle(sticks):
    arr = sorted(sticks)
    b = [-1]                                    #no triangle exist condition and last in seq returned
    for i in range(len(arr)-2):   
        a = arr[i:i+3]                          #slice array in indexes of 3 and assign to a
        if a[0] + a[1] > a[2]:                  #check triangle condition
            b = a                               #update b  
    return b                                    
                      
    
                               
                 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
