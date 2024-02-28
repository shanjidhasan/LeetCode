class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""
        i = 0
        while i<len(word1) or i<len(word2):
            if  i<len(word1):
                ans = ans+word1[i]
            if  i<len(word2):
                ans = ans+word2[i]
            i+=1
        return ans
