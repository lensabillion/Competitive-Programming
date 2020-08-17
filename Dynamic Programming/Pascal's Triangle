class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        answer = []
        if numRows == 0:
            return answer
        answer = [[1]]
        for i in range(1,numRows):
            prev = answer[-1]
            row = [1]
            for j in range(1,i):
                row.append(prev[j-1] + prev[j])
            row.append(1)
            answer.append(row)
        
        return answer
                
