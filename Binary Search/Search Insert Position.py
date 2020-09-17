class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        #O(N)
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
        if nums[len(nums)-1] < target:
                return len(nums)
        if nums[0]> target:
                return 0
        for i in range(0,len(nums)-1):
             
            if nums[i] < target and nums[i+1] > target:
                return i+1
        """
        #O(log n)
        low = 0
        high =  len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
        
