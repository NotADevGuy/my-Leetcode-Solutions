class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        trash = []
        bestLength = 0
        while s:
            for char in s:
                if char not in trash:
                    trash.append(char)
                elif char in trash:
                    break
            if len(trash) > bestLength:
                bestLength = len(trash)
            trash = []
            s.pop(0)
        return bestLength