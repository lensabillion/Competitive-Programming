#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    p = 0
    for i in n:
        p += int(i)
    p = p * k
    def sum_cal(p):
        if p <= 9:
            return p
        else:
            sum = 0
            while p:
                sum += p % 10
                p = p // 10
        return sum_cal(sum)
   
    return sum_cal(p)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
