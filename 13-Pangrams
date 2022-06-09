#!/bin/python3

import math
import os
import random
import re
import sys

#Complete the function pangrams in the editor below. It should return the string 
#pangram if the input string is a pangram. 
# Otherwise, it should return not pangram.


def pangrams(s):
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in a:
        if i not in s.lower():
            return "not pangram"
  
    return  "pangram"
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
