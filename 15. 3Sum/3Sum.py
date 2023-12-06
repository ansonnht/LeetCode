class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        visited = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if nums[i] in visited:
                continue
            else:
                visited.add(nums[i])
            l, r = i + 1, len(nums)-1
            while l < r:
                curr_sum = nums[l] + nums[r] + nums[i]
                if  curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
