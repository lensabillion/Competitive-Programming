class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False
        row = len(matrix)
        col = len(matrix[0])
        
        low = 0
        high = row * col - 1
        

        while low <= high:
            mid =   (low + high) //2
            if matrix[mid/col][mid%col] == target:
                return True
            if matrix[mid/col][mid%col] < target:
                low = mid + 1
                
            if matrix[mid/col][mid%col] > target:
                high = mid-1
            
        return False
            
