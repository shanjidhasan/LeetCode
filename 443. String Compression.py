class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ch = [chars[0]]
        freq = [1]
        chi = 0
        for i in range(1,len(chars)):
            if chars[i] == ch[chi]:
                freq[chi]+=1
            else:
                ch.append(chars[i])
                freq.append(1)
                chi+=1
        ans = []
        j = 0
        for i in range(len(ch)):
            
            chars[j] = (str(ch[i]))
            j+=1
            if freq[i]>1: 
                ds = str(freq[i])
                for d in ds:
                    chars[j] = d
                    j+=1
        n = len(chars)
        while j<n:
            del chars[-1]
            j+=1
        return len(chars)
        
