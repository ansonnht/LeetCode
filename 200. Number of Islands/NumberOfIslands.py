class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for r_move, c_move in directions:
                dfs(r + r_move, c + c_move)
        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    cnt += 1
                    dfs(r, c)
        return cnt
