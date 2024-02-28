class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        mc = max(candies)
        ans = []
        for c in candies:
            if c+extraCandies>=mc:
                ans.append(True)
            else:
                ans.append(False)
        return ans
