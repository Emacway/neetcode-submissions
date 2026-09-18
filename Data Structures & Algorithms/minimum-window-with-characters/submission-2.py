class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # hashmap sliding window method
        if t == "":
            return ""

        countT = {} #frequency of each character in t
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        

        l = 0
        window = {} #counts for current window
        have = 0 #how many characters currently meet the required count
        need = len(countT) #how many distinct characters we need to match
        res = [-1, -1] # best window indices
        reslen = float("infinity") #length of best window (want to minimize)


        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need: # we have a valid window!
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        if res == [-1, -1]:
            return ""
        else:
            return s[res[0]:res[1] + 1]