##Given an array of integers, 
#calculate the ratios of its elements that are positive, negative, and zero. 
#Print the decimal value of each fraction on a new line with  places after the decimal.##
import math
import os
import random
import re
import sys


def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0 :
            neg += 1
        else:
            zero += 1
        
    print(f'{pos/len(arr):.6f}')
    print(f'{neg/len(arr):.6f}')
    print(f'{zero/len(arr):.6f}')
      
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
