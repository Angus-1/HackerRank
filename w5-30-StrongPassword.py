#!/bin/python3

import math
import os
import random
import re
import sys


#Its length is at least .
#It contains at least one digit.
#It contains at least one lowercase English character.
#It contains at least one uppercase English character.
#It contains at least one special character. The special characters are: !@#$%^&*()-+
#returns min number of chars to make password strong

def minimumNumber(n, pw):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    cnt=0 #increment count if any condition not met
    
    if len(pw)<6:
        cnt=6-len(pw)
    if pw.count(upper_case)==0:
        if cnt<1:
            cnt+=1
    if pw.count(lower_case)==0:
        if cnt<1:
            cnt+=1
    if pw.count(special_characters)==0:
        if cnt<1:
            cnt+=1
    return cnt

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
