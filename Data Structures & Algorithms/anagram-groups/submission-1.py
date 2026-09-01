class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        CharFreqToStrings = {}
        for s in strs:
            charFreq = [0] * 26
            for ch in s:
                charFreq[ord(ch) - ord('a')] += 1
            if tuple(charFreq) not in CharFreqToStrings:
                CharFreqToStrings[tuple(charFreq)] = [s]
            elif tuple(charFreq) in CharFreqToStrings:
                CharFreqToStrings[tuple(charFreq)].append(s)
        result = []
        for key in CharFreqToStrings:
            result.append(CharFreqToStrings[key])

        return result