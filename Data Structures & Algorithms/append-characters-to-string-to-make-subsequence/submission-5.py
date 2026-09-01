class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # initialize pointers
        i = 0
        j = 0 

        while (i < len(s)) and (j < len(t)): #stay in bounds
            if s[i] == t[j]: #if we match, increment both
                i += 1
                j += 1
            else: # if we don't match, increment i only
                i += 1
        # j is the first index of a different char in t
        # rest of chars in t need to be appended
        return len(t) - j

    