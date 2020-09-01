class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
      
        list =[]
        if len(A) != len(B):
            return False
        if len(A)<2  and len(B)<2:
           
            return False
        if len(A)==2  and len(B)==2:
            if A[0] == B[1] and A[1] == B[0]:
                return True
            return False
        if A == B:
            dict = {}
            for i in range(len(A)):
                if A[i] not in dict:
                    dict[A[i]] = 0
                dict[A[i]] += 1
            for k in dict:
                if dict[k] >= 2:
                    return True
               
        for i in range(len(A)):
           
            if A[i] != B[i]:
                list.append(i)
        if len(list) == 2:
            temp = A[:list[0]]+A[list[1]]+A[list[0]+1:list[1]] + A[list[0]] +A[list[1]+1:]
           
            if temp == B:
                return True
             
        
