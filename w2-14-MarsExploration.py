#Expected signal: SOSSOSSOSSOS
#Recieved signal: SOSSPSSQSSOR
#We print the number of changed letters, which is 3

#!/bin/python3

import math
import os
import random
import re
import sys

def marsExploration(s):
    changed = 0
    for i in range(0,len(s),3):
     if s[i] != 'S': changed += 1
     if s[i+1] != 'O': changed += 1
     if s[i+2] != 'S': changed += 1
    return changed
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

