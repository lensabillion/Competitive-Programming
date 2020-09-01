class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort by first element
        if intervals == []:
            return []
        """
        O(N^2) sorting
        for i in range(len(intervals)-1):
            index = i
            for j in range(i+1,len(intervals)):
                if intervals[j][0] < intervals[index][0]:
                    index = j
            intervals[i],intervals[index] = intervals[index],intervals[i]
        """
        intervals.sort(key=lambda x: x[0])
        ans =[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= ans[-1][1] and intervals[i][1] > ans[-1][1] :
                ans[-1][1] = intervals[i][1]
            elif intervals[i][0] <= ans[-1][1] and intervals[i][1] <= ans[-1][1]:
                ans[-1][1] = ans[-1][1]
            else:
                ans.append(intervals[i])
        return ans
