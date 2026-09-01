class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #map nums to their frequencies
        numCount = {}
        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        
        #list of [frequency, num] pairs
        freqList = []
        for key, freq in numCount.items():
            freqList.append([freq, key])
        freqList.sort()
        
        res = []
        while (k > 0):
            res.append(freqList.pop()[1])
            k -= 1
        
        return res
