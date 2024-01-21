class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."]*n for i in range(n)]
        def backtrack(r):
            if r == n:
                valid_board = ["".join(i) for i in board]
                res.append(valid_board)
                return
            for c in range(n):
                if c in col or (r - c) in negDiag or (r + c) in posDiag:
                    continue
                col.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                board[r][c] = "Q"
                backtrack(r + 1)
                col.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                board[r][c] = "."
        backtrack(0)
        return res
