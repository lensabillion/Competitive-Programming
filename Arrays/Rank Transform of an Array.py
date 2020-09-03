class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        new = sorted(set(arr))
        dict = {}
        for i in new:
            if i not in dict:
                dict[i] = len(dict) + 1
       
        for num in arr:
            ans.append(dict[num])
        return ans
                
            
