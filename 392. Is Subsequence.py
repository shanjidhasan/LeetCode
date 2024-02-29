class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        si = 0
        if len(s) == 0:
            return True
        for c in t:
            if s[si] == c:
                si+=1
                if si == len(s):
                    return True
        return False
