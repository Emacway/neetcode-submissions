class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) solution
        numSet = set(nums) #remove duplicates
        longest = 0 #length of longest consecutive sequence
        for num in numSet:
            if num - 1 not in numSet: #num is the start of a sequence
                length = 1
                while num + length in numSet:
                    length += 1
                if length > longest:
                    longest = length
        return longest
