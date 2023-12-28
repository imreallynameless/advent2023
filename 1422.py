
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        size = len(s)

        for i in range(1, size):
            [left, right] = [s[:i], s[i:]]
            left = left.count('0')
            right = right.count('1')
            print(left, right)
            sum = max(s, left+right)

        return sum