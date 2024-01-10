class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(node, curr_path):
            curr_path.append(node)
            if node == len(graph) - 1:
                res.append(curr_path.copy())
            for neighbor in graph[node]:
                dfs(neighbor, curr_path)
                curr_path.pop()
        dfs(0, [])
        return res

