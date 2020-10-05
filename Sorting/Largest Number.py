class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        #Change ever entery to string
        #1.sort by first number
        #2.Sort by their second number 
        #3.concatinate
        
        str_arr = []
        for i in nums:
            str_arr.append(str(i))
       
            
        if len(nums) == 1:
            return str_arr[-1]
        for i in range(len(str_arr)):
            for j in range(i+1 ,len(str_arr)):
                  
                if  str_arr[i]+str_arr[j] < str_arr[j]+str_arr[i] :
                   
                    str_arr[i],str_arr[j] =str_arr[j],str_arr[i]
                    
        ans = ''.join(str_arr)
        if int(ans) == 0:
            return "0"
        else:
            return ans
