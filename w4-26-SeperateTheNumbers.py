#!/bin/python3

import math
import os
import random
import re
import sys

def separateNumbers(s):
    current = s[0]
    length = 0
    first = 0
    
    while len(current) < len(s) // 2:
        test = current = s[:length + 1]
        first = int(current)
        
        n = 1
        while len(test) < len(s): 
            test += str(int(current) + n) 
            n += 1
        
        if test == s: 
            print("YES", first)
            return True
        
        length += 1
        testStr = ""
        
    print("NO")
    
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
