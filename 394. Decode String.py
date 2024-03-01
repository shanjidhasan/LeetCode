class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_str, current_num = "", 0
            elif char == ']':
                prev_str, repeat_count = stack.pop()
                current_str = prev_str + repeat_count * current_str
            else:
                current_str += char

        return current_str
