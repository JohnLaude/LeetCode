class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        a = []
        if len(s) < 1:
            count = 0
        elif len(s) == 1:
            count = 1
        else:
            for i  in range(len(s) - 1):
                a.append(s[i])
                while s[i + 1] in a:
                    if len(a) > count:
                        count = len(a)
                    a.pop(0)    
            a.append(s[len(s) - 1])
        if len(a) > count:
            count = len(a)
        return count