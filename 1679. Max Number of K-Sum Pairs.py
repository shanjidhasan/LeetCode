class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        freq = Counter(nums)
        dij = set()
        for i in freq:
            if i not in dij and k-i in freq:
                if i == (k-i):
                    ans+=freq[i]//2
                else:
                    ans+=min(freq[i], freq[k-i])
                dij.add(i)
                dij.add(k-i)
        return ans
