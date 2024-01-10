class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        n = len(isConnected)
        def dfs(node):
            isConnected[node][node] = 0
            for node_2 in range(n):
                if isConnected[node][node_2] == 1:
                    isConnected[node][node_2] = 0
                    dfs(node_2)
        for i in range(n):
            if isConnected[i][i] == 1:
                res += 1
                dfs(i)
        return res
