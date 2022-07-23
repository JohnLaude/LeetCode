class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        centers = [len(s) - 1]
        for diff in range(1,len(s)):
            centers.append(centers[0] + diff)
            centers.append(centers[0] - diff)
        
        for center in centers:
            if (min(center + 1, 2 * len(s) - 1 - center) <= len(longest)):
                break
            
            if center % 2 == 0:
                left, right = (center // 2) -1, (center // 2) + 1
            else:
                left, right = (center // 2), (center // 2) + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len(longest):
                longest = s[left + 1: right]
        
        return longest