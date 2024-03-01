class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt=0
        transpose = [list(row) for row in zip(*grid)]
        for row in grid:
            cnt+=transpose.count(row)
        return cnt
