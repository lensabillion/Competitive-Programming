class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums)//2
                L = nums[:mid]
                R = nums[mid:]
                mergeSort(L)
                mergeSort(R)
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        nums[k] = L[i]
                        i += 1
                    else:
                        nums[k] =R[j]
                        j += 1
                    k += 1

                while i < len(L):
                    nums[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    nums[k] = R[j]
                    j += 1
                    k += 1
            return nums
        return mergeSort(nums)
