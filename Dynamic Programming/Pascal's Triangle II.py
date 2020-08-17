class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        answer = [[1]]
       
        for i in range(1,rowIndex+1):
            prev = answer[-1]
            row = [1]
            for j in range(1,i):
                row.append(prev[j-1] + prev[j])
            row.append(1)
            answer.append(row)
        
        return answer[-1]
        
      
