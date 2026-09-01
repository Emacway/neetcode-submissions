class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #O(nlogn) solution
        if not nums:
            return 0 #if nums is empty, return 0
        res = 0 #longest streak initialized to 0
        nums.sort() #n log n runtime

        curr, streak = nums[0], 0 #initialize
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0 #start over streak at next number
            while i < len(nums) and nums[i] == curr: #repeats in nums
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res
        