class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if " " not in s:
            return len(s)
        res = 0
        i = len(s) - 1
        while (s[i] == " "):
            i -= 1
        # i is now index of last non-space character
        while (s[i] != " "):
            res += 1
            i -= 1
        return res
            