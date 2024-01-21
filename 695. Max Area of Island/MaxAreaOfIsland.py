class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
OBOBOB        cols = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for r_move, c_move in directions:
                 area += dfs(r + r_move, c + c_move)
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res
