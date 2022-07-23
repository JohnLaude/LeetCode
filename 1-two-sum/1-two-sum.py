class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, j in enumerate(nums):
            diff = target - j
            if (diff in nums) and (i != nums.index(diff)): 
                return i, nums.index(diff)