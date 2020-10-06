class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        left = 1 
        right = x - 1
        while True:
            mid  = (left + right)//2
            if mid > x/mid:
                right =mid- 1
            else:
                if mid + 1 > x/(mid + 1):
                    return mid
                left =mid+ 1
