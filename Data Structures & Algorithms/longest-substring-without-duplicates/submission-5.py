class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        i = 0
        longest = 0

        for j in range(len(s)):
            if s[j] in seen:
                i = max(seen[s[j]] + 1, i)
            seen[s[j]] = j
            longest = max(longest, j - i + 1)
        return longest