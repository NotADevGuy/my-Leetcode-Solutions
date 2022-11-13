class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        err = False
        tmp = ""
        s = s.lstrip()
        for item in s:
            if item.isdigit():
                tmp += item
                err = True
            elif err == True:
                break
            elif item == '-':
                tmp += '-'
            elif item == '+':
                tmp += '+'
            else:
                break
        try:
            tmp = int(tmp)
        except:
            return 0
        
        if tmp < (-2**31):
            return -2**31
        elif tmp > (2**31 - 1):
            return 2**31 - 1
        else:
            return tmp
        
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