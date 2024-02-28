class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n = min(len(str1), len(str2))
        for i in range(n, 0, -1):
            sub = str1[0:i]
            n1 = len(str1)/len(sub)
            n2 = len(str2)/len(sub)
            j = 0
            s1 = ""
            s2 = ""
            while j<n1 or j<n2:
                if j<n1:
                    s1+=sub
                if j<n2:
                    s2+=sub
                j+=1
            if str1 == s1 and str2 == s2:
                return sub
        return ""

        
