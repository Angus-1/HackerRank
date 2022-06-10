#If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of .
#If the value of  is less than 38, no rounding occurs as the result will still be a failing grade.
 
 
 #!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):

    rounded = []

    for i in grades:
        d = i % 5       

        if (i < 38) or (d < 3):     
            rounded.append(i)
        else:
            result = i + (5 - d)
            rounded.append(result)

    return rounded
                   
     
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
