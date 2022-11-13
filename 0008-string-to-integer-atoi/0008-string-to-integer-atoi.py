class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        neg = False
        s = s.lstrip()
        tmp = ''
        
        if len(s) == 0:
            return 0
        if s[0] == '-':
            s = s[1:]
            neg = True
        elif s[0] == '+':
            s = s[1:]
        for letter in s:
            if letter.isdigit():
                tmp += letter
            else:
                break

        try:
            tmp = int('-' + tmp) if neg else int(tmp)
            if tmp < (-2**31):
                return -2**31
            elif tmp > (2**31 - 1):
                return 2**31 - 1
        except:
            return 0

        return tmp

        
        
        """
        neg = False
        nums = []
        s = s.lstrip()
        tmp = ''
        if len(s) == 0:
            return 0
        if s[0] == '-':# or s[0] == '+':
            s = s[1:]
            neg = True
        elif s[0] == '+':
            s = s[1:]
        for letter in s:
            if letter.isdigit():
                tmp += letter
            elif not letter.isdigit():
                break

        try:
            if neg:
                tmp = int('-' + tmp)
                if tmp < (-2**31):
                    tmp = -2**31
            else:
                tmp = int(tmp)
                if tmp > (2**31 - 1):
                    tmp = (2**31 - 1)
        except:
            return 0

        return tmp
        """