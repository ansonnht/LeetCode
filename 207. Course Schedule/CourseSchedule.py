class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for post, pre in prerequisites:
            graph[post].append(pre)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if len(graph[node]) == 0:
                return True
            visited.add(node)
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            visited.remove(node)
            graph[node] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
