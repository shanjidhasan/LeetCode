class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        f = 0
        for x in nums:
            if x == 0:
                f+=1
                if f>1:
                    return [0]*len(nums)
            else:
                product *= x
        ans = []
        for x in nums:
            if f and x != 0:
                ans.append(0)
            elif x!=0:
                ans.append(product/x)
            else:
                ans.append(product)
        return ans
        
