class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            if right - left + 1 - max(count.values()) <= k:
                res = max(right - left + 1, res)
            else:
                count[s[left]] -= 1
                left += 1
        return res
