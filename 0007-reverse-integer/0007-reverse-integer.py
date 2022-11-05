class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)[::-1]
        if x[-1] == '-':
            x = str('-' + x[:-1])

        if int(x) > ((2**31) - 1) or int(x) < (-2**31):
            return 0
        else:
            return int(x)