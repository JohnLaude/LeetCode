class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Initialize first string as prefix
        prefix = strs[0]
 
        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                # make prefix smaller each time they do not equal the next string
                prefix = prefix[:len(prefix)-1]
        return prefix