class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_node = {}
        def dfs(node):
            if node in safe_node:
                return safe_node[node]
            safe_node[node] = False
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            safe_node[node] = True
            return safe_node[node]
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
