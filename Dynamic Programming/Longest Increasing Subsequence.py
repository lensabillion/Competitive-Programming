class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        #this is O(n^2) solution
        memo = [0] * len(nums)
        for k in range(len(nums)):
            memo[k] = 1
            for i in range(k):
                if nums[i] < nums[k]:
                    memo[k] = max(memo[k],memo[i]+1)
        return max(memo)
       """
        #this one is O(nlogn) solution
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            i = 0
            j = size
            while i != j:
                m = (i + j) / 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            size = max(i + 1, size)
            
        return size
