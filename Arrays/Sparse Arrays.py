def matchingStrings(strings, queries):
    ans = [0] * len(queries)
    for q in range(len(queries)):
        for s in range(len(strings)):
            if queries[q] == strings[s]:
                ans[q] += 1
    return ans
