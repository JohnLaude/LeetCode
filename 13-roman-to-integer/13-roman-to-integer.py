class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0;
        for i, j in enumerate(s):
            if (j == "I"):
                sum += 1
                if i < len(s) -1:
                    if (s[i+1] == "V"):
                        sum -= 2
                    elif (s[i+1] == "X"):
                        sum -= 2
            if (j == "V"):
                sum += 5
            if (j == "X"):
                sum += 10
                if i < len(s) -1:
                    if (s[i+1] == "L"):
                        sum -= 20
                    elif (s[i+1] == "C"):
                        sum -= 20
            if (j == "L"):
                sum += 50
            if (j == "C"):
                sum += 100
                if i < len(s) -1:
                    if (s[i+1] == "D"):
                        sum -= 200
                    elif (s[i+1] == "M"):
                        sum -= 200
            if (j == "D"):
                sum += 500
            if (j == "M"):
                sum += 1000
        return sum
                
                
            