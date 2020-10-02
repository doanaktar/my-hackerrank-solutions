#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    liked = 0
    shared = 5
    count = 0
    for i in range(0, n):        
        liked = math.floor(shared/2)
        shared = liked * 3
        count += liked
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
