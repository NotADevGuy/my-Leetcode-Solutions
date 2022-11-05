class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        import itertools
        if len(digits) == 0:
            return []
        letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        digits = [list(letters[letter]) for letter in list(digits)]
        return [''.join(item) for item in list(itertools.product(*digits))]