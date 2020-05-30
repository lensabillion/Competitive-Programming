class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        """
        :Time Complexity:O(n)
        :Space Complexity:O(n)
        """
      
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i 
        for i in range(len(nums)):
            if target - nums[i] in dict:
                if i != dict[target - nums[i]]:
                    return [i,dict[target - nums[i]]]
    
