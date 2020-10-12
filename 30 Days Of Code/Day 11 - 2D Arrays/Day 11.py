#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    sums = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(4):
        for j in range(4):
            hourglass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i + 1][j + 1] + arr[i +2][j] + arr[i+2][j+1] + arr[i+2][j+2]            
            sums.append(hourglass)    
   
    print(max(sums))
        
'''
a = [map(int, raw_input().split()) for i in xrange(6)]
print max(a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2] for i in xrange(4) for j in xrange(4))
'''
        
