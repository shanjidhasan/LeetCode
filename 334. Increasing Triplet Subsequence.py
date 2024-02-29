class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = None
        j = None
        for n in nums:
            if i == None or n<=i:
                i=n
            elif j == None or n<=j:
                j=n
            else:
                return True
        return False
