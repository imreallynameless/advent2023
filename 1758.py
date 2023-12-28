class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0

        length = len(s)
        for i in range(length):
            if i % 2 == 0:
                if s[i] == '1':
                    sum += 1
            else:
                if s[i] == '0':
                    sum += 1
        sum = min(sum, length - sum)
                
        return sum