#!/bin/python3

import math
import os
import random
import re
import sys

#current array   ( 1 1 1 2 2 2 3 3 )
#current colors  (1, 2, 3)
def sockMerchant(n, ar):
    colors:set = set(ar) #make set of all possible colors
    pairs:int = 0        #num of curr pairs 0
    for c in colors:     #use colors to iterate through ar 
        pairs += ar.count(c) // 2   #count returns number of each colors total occurences
                                     #and we divide by 2 with floor operator giving us pairs without extras 
        
    return pairs 
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
