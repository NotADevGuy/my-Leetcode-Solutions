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
            elif item in ('-', '+'):
                tmp += item
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