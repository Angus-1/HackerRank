import math
import os
import random
import re
import sys
#given an array find its median

def findMedian(arr):
    arr = sorted(arr)
    return arr[len(arr)//2] #use floor division operator for oddcase


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
