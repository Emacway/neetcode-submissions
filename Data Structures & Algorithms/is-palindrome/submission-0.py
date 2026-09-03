class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnumS = ""
        for ch in s:
            if ch.isalnum():
                c = ch.lower()
                alnumS += c
        
        n = len(alnumS)

        for i in range(n//2): #integer truncation
            if alnumS[i] != alnumS[n - 1 - i]:
                return False
        

        return True

        
        