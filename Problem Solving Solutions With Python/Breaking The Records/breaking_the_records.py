#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    minscore = 0
    maxscore = 0
    for i in range(1, len(scores)):
        if scores[i] < minimum:
            minscore += 1
            minimum = scores[i]
        elif scores[i] > maximum:
            maxscore += 1
            maximum = scores[i]
    return maxscore, minscore



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
