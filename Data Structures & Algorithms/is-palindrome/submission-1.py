class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnumS = ""
        for ch in s:
            if ch.isalnum():
                c = ch.lower()
                alnumS += c
        
        return alnumS == alnumS[::-1] # reverse