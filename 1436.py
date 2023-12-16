class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        routes = {}
        for path in paths:
            routes[path[0]] = path[1]
        for path in paths:
            if routes.get(path[1]) == None:
                return path[1]