class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for start, end in connections:
            if start not in graph: graph[start] = {}
            if end not in graph: graph[end] = {}
            graph[start][end] = 1
            graph[end][start] = 0
        visited = set()
        def dfs(node):
            res = 0
            visited.add(node)
            if node in graph:
                for neighbor in graph[node].keys():
                    if neighbor not in visited:
                        res += graph[node][neighbor] + dfs(neighbor)
            return res
        return dfs(0)
