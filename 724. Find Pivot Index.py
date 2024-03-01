class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        prefix_sum = 0

        for i, num in enumerate(nums):
            if prefix_sum == total_sum - prefix_sum - num:
                return i
            prefix_sum += num

        return -1
