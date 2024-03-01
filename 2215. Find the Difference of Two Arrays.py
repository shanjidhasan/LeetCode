class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        answer = [
            list(set_nums1 - set_nums2),
            list(set_nums2 - set_nums1)
        ]

        return answer
