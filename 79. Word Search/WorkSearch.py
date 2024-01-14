class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r_max = len(board)
        c_max = len(board[0])
        visited = set()
        def dfs(r, c, curr):
            if curr == len(word):
                return True
            if r not in range(r_max) or c not in range(c_max) or word[curr] != board[r][c] or (r, c) in visited:
                return False
            visited.add((r,c))
            direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            res = False
            for r_move, c_move in direction:
                res = res | dfs(r + r_move, c + c_move, curr + 1)
            visited.remove((r, c))
            return res
        ## Accelerate
        counter = {}
        for r in range(r_max):
            for c in range(c_max):
                if board[r][c] in counter: counter[board[r][c]] += 1
                else: counter[board[r][c]] = 1
        w_counter = {}
        for l in word:
            if l in w_counter: w_counter[l] += 1
            else: w_counter[l] = 1
        for l, c in w_counter.items():
            if l not in counter or counter[l] < c:   
                return False
        ##
        for r in range(r_max):
            for c in range(c_max):
                if dfs(r, c, 0):
                    return True
        return False
