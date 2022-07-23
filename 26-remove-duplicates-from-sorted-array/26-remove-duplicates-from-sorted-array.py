class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_set = set()
        for i,j in enumerate(nums):
            new_set.add(j)
        count = 0
        while True:
            if count == len(nums) - 1:
                break
            if nums[count] == nums[count + 1]:
                nums.pop(count + 1)
            else:
                count += 1
        return len(new_set)