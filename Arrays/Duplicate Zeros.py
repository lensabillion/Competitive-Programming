class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zero_count = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                zero_count += 1
       
        for i in range(len(arr)-1,-1,-1):
            if i + zero_count < len(arr):
                arr[i+zero_count] = arr[i]
            if arr[i] == 0:
                zero_count -= 1
                if i + zero_count < len(arr):
                    arr[i+zero_count] = 0
       
