class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        def dfs(n, curr):
            if sum(curr) == target:
                res.append(curr[:])
                return 
            elif sum(curr) > target or n == len(candidates):
                return
            curr.append(candidates[n])
            dfs(n + 1, curr)
            curr.pop()
            while n + 1 < len(candidates) and candidates[n] == candidates[n + 1]:
                n += 1
            dfs(n + 1, curr)
        dfs(0, [])
        return res
