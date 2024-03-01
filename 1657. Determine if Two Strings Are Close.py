class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        def get_char_freq(word):
            char_freq = {}
            for char in word:
                char_freq[char] = char_freq.get(char, 0) + 1
            return char_freq

        freq1 = get_char_freq(word1)
        freq2 = get_char_freq(word2)

        if set(freq1.keys()) != set(freq2.keys()):
            return False

        return sorted(freq1.values()) == sorted(freq2.values())
