#!/bin/python3

import math
import os
import random
import re
import sys

# Given an array of bird sightings where every element represents a bird type id,
# determine the id of the most frequently sighted type. 

# If more than 1 type has been spotted that maximum amount, return the #smallest of their ids.

def migratoryBirds(arr):
   
    birds = set(arr)  #set of unique bird ids
    most = 0         #most occured bird
    maxID = 0        #maxid key we assign to bird element we are at
    
    for b in birds:                 #iterate by unique bird IDs
        if arr.count(b) > most:     #compare count of current bird to most occured bird 
            most = arr.count(b)     #update count of most occured bird 
            maxID = b               #max id is equal to current b element
    return maxID                    #return maxID bird which also stopped at most occured bird
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
