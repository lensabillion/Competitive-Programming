#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    stack = []
    max_days = 0
    for i in p:
        alive = 0
        while stack and i <= stack[-1][0]:
            alive = max(alive,stack.pop()[1])
        
        if not stack:
            alive = 0
        else:
            alive += 1

        max_days = max(max_days,alive)
        stack.append([i,alive])
    return max_days


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
