class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        over = 0
        m = 1
        neg = False
        if x < 0: 
            x *= -1
            neg = True
        n = len(str(x)) - 1
        while n >= 0:
            over = x%(10**m)/(10**(m-1))
            x = x - over
            result += (over*(10**(n)))
            m += 1
            n -= 1
        if neg is True:
            result *= -1
        if (result < -2**31) or (result > 2**31 -1):
            return 0
        return result
        