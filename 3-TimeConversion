#!/bin/python3

import math
import os
import random
import re
import sys
#Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock

def timeConversion(s): 
    if s[8] == 'A' and s[0:2] == '12': 
        return f"00{s[2:-2]}"
    elif s[8] == 'P' and s[0:2] != '12': 
        return f"{int(s[0:2]) + 12}{s[2:-2]}" 
    return s[0:8] 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
