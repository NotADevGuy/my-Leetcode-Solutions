class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):  # This manages outliers
            return s

        L = [''] * numRows  # Creates the rows
        index, step = 0, 1  # Provides an index for row and increment

        for char in s:  # AKA: For character in string provided
            L[index] += char  # For the current row, append the character
            if index == 0:  # If the row is first row...
                step = 1  # Set the increment to 1
            elif index == numRows - 1:  # Else if the row is the last one...
                step = -1  # Sets the increment to last
            index += step  # Row is incremented by stepper

        return ''.join(L)  # This just combines it all by using a string operator to combine contents of list.