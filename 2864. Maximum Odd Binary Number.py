class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_ones = s.count('1')

        if num_ones == 0:
            return s

        ans = [0]*(len(s)-num_ones)
        ans.append(1)
        ones = [1]*(num_ones-1)
        ones.extend(ans)
