class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        concat = nums1 + nums2
        concat.sort()
        median = 0.0
        if (len(concat) % 2) == 0:
            n = len(concat)
            med = float(concat[(n/2) - 1] + concat[(n/2)])
            median = med/2
        else:
            median = concat[len(concat)//2]
        return median