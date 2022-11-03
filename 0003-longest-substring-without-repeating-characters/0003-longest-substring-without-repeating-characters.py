class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        length, bestLength, trash = 0, 0, []
        while s:
            for char in s:
                if char not in trash:
                    trash.append(char)
                    length += 1
                elif char in trash:
                    break
            bestLength = length if length > bestLength else bestLength
            length, trash = 0, []
            s.pop(0)
        return bestLength