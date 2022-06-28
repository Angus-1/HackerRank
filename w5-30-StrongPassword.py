#!/bin/python3

import math
import os
import random
import re
import sys


#Its length is at least 6.
#It contains at least one digit.
#It contains at least one lowercase English character.
#It contains at least one uppercase English character.
#It contains at least one special character. The special characters are: !@#$%^&*()-+
#returns min number of chars to make password strong

def minimumNumber(x, password):
    minx = 6
    count = 0
    if not re.search('[0-9]', password): count += 1
    if not re.search('[A-Z]', password): count += 1
    if not re.search('[a-z]', password): count += 1 
    if not re.search(r'[!@#$%^&*()\-+]', password): count += 1
    
    return max(minx - len(password), count) if n < 6 else count


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
