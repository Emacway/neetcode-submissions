class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Inefficient solution
        if nums == []:
            return 0
        setOfNums = set(nums) #remove duplicates
        start = 0
        maxSeqLength = 0
        for num in setOfNums:
            if num - 1 not in setOfNums:
                start = num
            count = 1
            while start + 1 in setOfNums:
                count += 1
                start += 1
            if count > maxSeqLength:
                maxSeqLength = count

        return maxSeqLength
