##O(NQ)
def matchingStrings(strings, queries):
    ans = [0] * len(queries)
    for q in range(len(queries)):
        for s in range(len(strings)):
            if queries[q] == strings[s]:
                ans[q] += 1
    return ans
##O(N+Q)
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    dict ={}
    ans = [] 
    
    for querie in queries:
       
        dict[querie] = 0
    
    for string in strings:
        if string in dict:
            dict[string] += 1
    
    for i in dict:
        ans.append(dict[i])
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
