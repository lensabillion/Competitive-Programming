import math
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for num in nums:
            div = []
            i =1 
           
            while i <= math.sqrt(num):
                if num % i == 0:
                   
                    if num / i == i:
                        div.append(i)
                    else:
                        div.append(i)
                        div.append(num/i)
                
                i +=1
            if len(div) == 4:
                for j in div:
                    sum += j
        return sum
                
