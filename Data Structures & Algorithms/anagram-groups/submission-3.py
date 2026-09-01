class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        CharFreqToStrings = defaultdict(list)
        for s in strs:
            charFreq = [0] * 26
            for ch in s:
                charFreq[ord(ch) - ord('a')] += 1
            CharFreqToStrings[tuple(charFreq)].append(s)

        return list(CharFreqToStrings.values())