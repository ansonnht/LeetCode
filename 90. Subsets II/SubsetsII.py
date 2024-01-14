class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        def dfs(n , curr):
            if n == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[n])
            dfs(n + 1, curr)
            curr.pop()
            while n + 1 < len(nums) and nums[n] == nums[n + 1]:
                n += 1
            dfs(n + 1, curr)
        dfs(0, [])
        return res
