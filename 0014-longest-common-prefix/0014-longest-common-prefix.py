class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 1) or (''.join(strs) == strs[0]*len(strs)):
            return strs[0]
        longest = max(strs, key=len)
        for i in range(1, len(longest) + 1):
            for item in strs:
                if item[:i] != longest[:i]:
                    return longest[:i - 1]
        return ''