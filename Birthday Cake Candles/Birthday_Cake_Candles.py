#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar.sort(reverse = True)  #sorting descend
    tallest = ar[0]          #findig the tallest candle
    blowable = 0
    for i in range(len(ar)): #searching for if there is a candle at same height
        if ar[i] == tallest:
            blowable += 1
    return blowable

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
