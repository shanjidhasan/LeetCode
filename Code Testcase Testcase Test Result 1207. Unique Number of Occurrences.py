class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurrence_counts = {}

        for num in arr:
            occurrence_counts[num] = occurrence_counts.get(num, 0) + 1

        return len(occurrence_counts.values()) == len(set(occurrence_counts.values()))
