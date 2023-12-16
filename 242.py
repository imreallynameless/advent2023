class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        tDict = {}
        for char in s:
            if sDict.get(char) == None:
                sDict[char] = 0
            sDict[char] += 1
        for char in t:
            if tDict.get(char) == None:
                tDict[char] = 0
            tDict[char] += 1
        return sDict == tDict