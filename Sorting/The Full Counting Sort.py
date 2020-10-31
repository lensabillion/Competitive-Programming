#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    
    sorted_arr = [[] for _ in range(100)] 
    ans = ""
    for i in range(len(arr)//2):
        index = int(arr[i][0])
       
        sorted_arr[index].append("-")
    
    for i in range((len(arr)//2),len(arr)):
        index = int(arr[i][0])
        sorted_arr[index].append(arr[i][1])
    
    print(' '.join([' '.join(each) for each in sorted_arr if each]))
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
