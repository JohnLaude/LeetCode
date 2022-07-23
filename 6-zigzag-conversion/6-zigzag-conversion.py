class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        count = 0
        counter = 0
        adder = 1
        x = ''
        bucket= [''] * numRows
        while count < len(s):
            bucket[counter] += s[count]
            counter += adder 
            if (counter == numRows - 1) or (counter == 0):
                adder *= -1 
            count += 1
                
        for i in bucket:
            x += i
        return x


            