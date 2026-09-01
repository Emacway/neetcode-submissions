class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True # empty string is always a subsequence
        else:
            i = 0
            j = 0
            while(j < len(t)):
                if s[i] == t[j]:
                    i += 1 
                    if i == len(s):
                        return True
                j += 1
                
            return False