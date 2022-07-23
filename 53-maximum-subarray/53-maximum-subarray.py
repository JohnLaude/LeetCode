class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -1000000
        temp_sum = 0
        for i in nums: 
            if temp_sum > 0:
                temp_sum += i
            else:
                temp_sum = i
            max_sum = max(max_sum, temp_sum)
        return max_sum