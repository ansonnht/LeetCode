class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_ptr = 0
        max_length = 0
        substring = set()
        for i in range(len(s)):
            if s[i] not in substring:
                substring.add(s[i])
            else:
                max_length = max(max_length, len(substring))
                while s[i] in substring:
                    substring.remove(s[left_ptr])
                    left_ptr += 1
                substring.add(s[i])
        return max(max_length, len(substring))
