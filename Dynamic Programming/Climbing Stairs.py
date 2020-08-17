class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        memo = [0] * n
        memo[0] = 1
        memo[1] = 2
        for i in range(2,n):
            memo[i] = memo[i-2] + memo[i-1]
       
        return memo[-1]
