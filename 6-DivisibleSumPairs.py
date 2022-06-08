#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#  Given an array of integers and a positive integer k, determine 
#  the number of (i,j)  pairs where  (i<j) and ar[i] + ar[j]  is
#  divisible by k.
        
def divisibleSumPairs(n, k, ar):
  pairs=0
  for i in range(0, len(ar)):
    for j in range(i + 1,len(ar)):
      if i<j:
         if (ar[i]+ar[j]) % k==0:
           pairs+=1
  return pairs
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
