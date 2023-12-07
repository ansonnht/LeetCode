class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return
            subset.append(candidates[i])
            dfs(i, subset, total + candidates[i])
            subset.pop()
            dfs(i+1, subset, total)
        dfs(0, [], 0)
        return res
