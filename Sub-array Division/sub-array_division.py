#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    i = 0
    j = 1
    count = 0
    if len(s) < 2 and s[0] == d:
        return m
    elif len(s) < 2 and s[0] != d:
        return 0
    else:
        while i < 5:
            if s[i] + s[j] == d:
                count += 1
                i += 1
                j += 1
                if count == m:
                    break
                else:
                    continue
            else:
                i += 1
                j += 1
        return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
