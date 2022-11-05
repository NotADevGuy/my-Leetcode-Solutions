class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pars = ['()', '{}', '[]']
        for par in pars:
            x = list(par)
            if s.count(x[0]) != s.count(x[1]):
                return False
        for i in s:
            if i in '({[':
                stack.append(i)

            for par in pars:
                left, right = list(par)
                if i in par:
                    cl, cr = left, right
                if i == right and left != stack[-1] or len(stack) == 0:
                    return False

            if i == cr and cl == stack[-1]:
                stack.pop()

        return True if len(stack) == 0 else False