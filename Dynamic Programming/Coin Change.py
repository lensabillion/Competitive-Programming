class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        
        value =[0] * (amount +1 )
        for x in range(1,amount+1):
            value[x] = float('inf')
            for c in coins:
                if x - c >= 0 and value[x-c]+1 <value[x]:
                    value[x] = value[x-c] + 1
                  
           
        if value[-1] != float('inf'):
            return value[-1]
        else:
            return -1
