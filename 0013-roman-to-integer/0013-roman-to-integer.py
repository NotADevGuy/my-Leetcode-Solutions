class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        s = s.replace("CM", "DCCCC")
        s = s.replace("CD", "CCCC")

        s = s.replace("XC", "LXXXX")
        s = s.replace("XL", "XXXX")

        s = s.replace("IX", "VIIII")
        s = s.replace("IV", "IIII")

        for char in list(s):
            if char == "M":
                total += 1000
            elif char == "D":
                total += 500
            elif char == "C":
                total += 100
            elif char == "L":
                total += 50
            elif char == "X":
                total += 10
            elif char == "V":
                total += 5
            elif char == "I":
                total += 1
        return total