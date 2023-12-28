class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        array = []
        start = [0, 0]
        array.append(start)
        for i in range(len(path)):
            if path[i] == 'N':
                start = [start[0], start[1]+1]
            elif path[i] == 'S':
                start = [start[0], start[1]-1]
            elif path[i] == 'E':
                start = [start[0]+1, start[1]]
            elif path[i] == 'W':
                start = [start[0]-1, start[1]]
            if start in array:
                return True
            array.append(start)
        return False
