class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index, nums):
            if index == len(nums):
                res.append(nums.copy())
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                dfs(index + 1, nums)
                nums[index], nums[i] = nums[i], nums[index]
        dfs(0, nums)
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            if len(nums) == 1:
                return [nums.copy()]
            n = nums.pop(0)
            perms = self.permute(nums)
            for p in perms:
                p.append(n)
            res.extend(perms)
            nums.append(n)
        return res
