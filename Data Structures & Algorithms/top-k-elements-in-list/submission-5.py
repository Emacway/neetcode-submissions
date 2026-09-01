class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #map nums to their frequencies
        numCount = {}
        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)
        
        # index of array is frequency, value is list of nums with that freq
        frequencies = [[] for i in range(len(nums) + 1)] 
        # note: do NOT do [[]] * len(nums) because lists are mutable and 
        # are therefore copied by REFERENCE
        for num, freq in numCount.items():
            frequencies[freq].append(num) 
            # if I had done [[]] * len(nums) this would append num to ALL lists
        
        res = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                res.append(num)
                if len(res) == k:
                    return res


        