class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set("aeiou")
        max_vowel_count = 0

        current_vowel_count = sum(1 for char in s[:k] if char in vowels)
        max_vowel_count = max(max_vowel_count, current_vowel_count)

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_vowel_count -= 1

            if s[i] in vowels:
                current_vowel_count += 1

            max_vowel_count = max(max_vowel_count, current_vowel_count)

        return max_vowel_count
