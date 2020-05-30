class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) < 2:
            return False
        dict = {}
        for i in range(len(deck)):
            if deck[i] not in dict:
                dict[deck[i]] = 0
            dict[deck[i]] += 1
        values = dict.values()
        
        for X in range(2,len(deck)+1):
            if len(deck) % X == 0:
                if all(val % X == 0 for val in values ):

                    return True
        return False
