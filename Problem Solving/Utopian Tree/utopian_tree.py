#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    growth = 0
    for i in n:
        for j in range(0, i+1):
            if j % 2 == 0:
                growth += 1
            elif j % 2 == 1:
                growth *= 2
        return growth


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = list(map(int, input().rstrip().split()))

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
