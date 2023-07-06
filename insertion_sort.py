#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    num_to_ins = arr[-1]
    i = n - 2
    
    while (i >= 0) and (arr[i] > num_to_ins):
        arr[i+1] = arr[i]
        print(*arr)
        i -= 1
    
    arr[i+1] = num_to_ins
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
