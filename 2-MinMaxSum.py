#!/bin/python3
#Given five positive integers, find the minimum and maximum values
#that can be calculated by summing exactly four of the five #integers. Then print the respective minimum and maximum values as 
#a single line of two space-separated long integers.
import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    minSum, maxSum = 0,0
    arr.sort()
    for i in range(len(arr)-1):
        minSum+=arr[i]
    for i in range(1, len(arr)):
        maxSum+=arr[i]
    print(minSum, maxSum)
   

    
    
    
    
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
