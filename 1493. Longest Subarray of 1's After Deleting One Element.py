class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        current_length = 0
        prev_length = 0
        found_zero = False

        for i, num in enumerate(nums):
            if num == 1:
                current_length += 1
                found_zero = False
            else:
                if found_zero == True:
                    prev_length = 0
                found_zero = True
                max_length = max(max_length, prev_length+current_length)
                prev_length = current_length
                current_length = 0
        max_length = max(max_length, prev_length+current_length)
        return max_length if max_length!=len(nums) else max_length-1
