#!/bin/python3

import math
import os
import random
import re
import sys

#Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

def breakingRecords(scores):
    scoreMin, scoreMax= scores[0],scores[0] 
    recMinCT,recMaxCT=0,0 
    for i in scores:
        if i<scoreMin:   
            scoreMin=i   
            recMinCT+=1  
        if i>scoreMax:    
            scoreMax=i     
            recMaxCT+=1      
    return [recMaxCT,recMinCT]
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
