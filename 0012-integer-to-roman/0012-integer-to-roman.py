class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        chars = []
        while num > 0:
            if num >= 1000:
                # print("M")
                num -= 1000
                chars.append("M")
            elif num >= 500:
                # print("D")
                num -= 500
                chars.append("D")
            elif num >= 100:
                # print("C")
                num -= 100
                chars.append("C")
            elif num >= 50:
                # print("L")
                num -= 50
                chars.append("L")
            elif num >= 10:
                # print("X")
                num -= 10
                chars.append("X")
            elif num >= 5:
                # print("V")
                num -= 5
                chars.append("V")
            elif num >= 1:
                # print("I")
                num -= 1
                chars.append("I")
        chars = ''.join(chars)
        chars = chars.replace("DCCCC", "CM")
        chars = chars.replace("CCCC", "CD")

        chars = chars.replace("LXXXX", "XC")
        chars = chars.replace("XXXX", "XL")

        chars = chars.replace("VIIII", "IX")
        chars = chars.replace("IIII", "IV")

        return chars