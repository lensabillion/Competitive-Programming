class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        ##O(N^2)
        count = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] < 0:
                    count += 1
        return count
        """
        ##O(M + N)
        m = len(grid)
        n = len(grid[0])
        count =0
        r = 0
        c = n-1
        while r < m and c >= 0:
            if grid[r][c] < 0:
                count += m -r
                c = c -1
            else:
                r = r + 1
        return count
