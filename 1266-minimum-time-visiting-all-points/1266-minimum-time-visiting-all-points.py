class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        n = 0
        m = 1
        while m < len(points): 
            diff_x = points[n][0] - points[m][0]
            diff_y = points[n][1] - points[m][1]
            if diff_y < 0:
                diff_y *= -1
            if diff_x < 0:
                diff_x *= -1
            temp = max(diff_x, diff_y)
            time += temp
            m += 1
            n += 1
            
        return time
            
        