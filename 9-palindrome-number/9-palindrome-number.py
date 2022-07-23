class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        i = 0 
        j = len(a) - 1
        while i < j: 
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1
        return True