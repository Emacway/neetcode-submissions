class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #map nums to their frequencies
        numCount = {}
        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)
        
        # min-heap to store frequencies
        heap = []
        for num, freq in numCount.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while (heap != []):
            res.append(heapq.heappop(heap)[1])
        
        return res
