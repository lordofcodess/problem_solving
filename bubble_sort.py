import math
import os
import random
import re
import sys

def countSwaps(a):
    Swaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j+1],a[j] = a[j], a[j+1]
                Swaps+=1
    print("Array is sorted in",Swaps,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[len(a)-1])
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
