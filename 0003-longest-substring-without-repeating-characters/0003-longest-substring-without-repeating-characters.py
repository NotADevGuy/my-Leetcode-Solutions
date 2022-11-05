class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        start = 0
        maxlength = 0
        for i, char in enumerate(s):
            if char in seen and start <= seen[char]:
                start = seen[char] + 1
            else:
                maxlength = max(maxlength, (i - start + 1))
            seen[char] = i
        return maxlength
    
        """
        for i in range(len(s)):
            if s[i] in seen and start <= seen[s[i]]:
                start = seen[s[i]] + 1
            else:
                maxlength = max(maxlength, (i - start + 1))
            seen[s[i]] = i
        return maxlength"""