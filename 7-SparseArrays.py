#!/bin/python3

import math
import os
import random
import re
import sys

#There is a collection of input strings and a collection of query strings. 
#For each query string, determine how many times it occurs in the list of input strings. 
#Return an array of the results.

def matchingStrings(strings, queries):
    return [strings.count(i) for i in queries]
    #.count method returns number each time element occurs in queries list 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
