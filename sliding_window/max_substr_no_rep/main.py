class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_len = 0
        max_len = 0
        seen = {}
        left = 0
        for i in range(len(s)):
            if s[i] in seen:
                left = max(left, seen[s[i]] + 1)

            seen[s[i]] = i
            cur_len = i - left + 1
            max_len = max(max_len, cur_len)
        return max_len
