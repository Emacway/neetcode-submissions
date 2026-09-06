class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two pointer O(n^2) solution, more clear code

        res = [] #initialize result
        nums.sort() #O(nlogn) runtime

        for i, a in enumerate(nums):
            if a > 0: #sorted nums so all remaining numbers are positive
                break 
            
            if i > 0 and a == nums[i - 1]: #skip duplicate values for the first number
                continue
            
            l = i + 1 #left pointer
            r = len(nums) - 1 #right pointer

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0: #too small, increment left
                    l += 1
                elif threeSum > 0: #too big, decrement right
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r: #skip duplicates
                        l += 1
            
        return res