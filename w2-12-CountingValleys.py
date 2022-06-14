#!/bin/python3

import math
import os
import random
import re
import sys

#==========================================================
#Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
# Sample Input
#8
#UDDDUDUU

#Sample Output
#1

#Explanation
#If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

#_/\      _
#   \    /
#    \/\/   
#==========================================================

def countingValleys(steps, path):
    count = 0
    altitude = 0
    for i in path:
        if i == "D":
            if altitude == 0:
                count += 1
            altitude -= 1
        else:
            altitude += 1
    return count  
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
