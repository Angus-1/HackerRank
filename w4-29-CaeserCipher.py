#!/bin/python3

import math
import os
import random
import re
import sys


def caesarCipher(s, k):
    a=''
    for i in s:
        if i.islower(): #lowercase letters
            a+=chr(((ord(i)-97+k)%26) + 97)  
        elif i.isupper(): #uppercase letters
            a+=chr(((ord(i)-65+k)%26) + 65)
        else:   # append any other chars
            a+=i
    return a
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
