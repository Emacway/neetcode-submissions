class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #map nums to their frequencies
        numCount = {}
        for num in nums:
            if num not in numCount:
                numCount[num] = 1
            else:
                numCount[num] += 1
        
        #invert the map: key = frequency, value = list of nums 
        freqMap = defaultdict(list)
        for num in numCount:
            freqMap[numCount[num]].append(num)
        
        res = []
        while (k > 0):
            maxFreq = max(freqMap.keys())
            res.append(freqMap[maxFreq].pop(0))
            if freqMap[maxFreq] == []:
                del freqMap[maxFreq]
            k -= 1
        
        return res

                
        