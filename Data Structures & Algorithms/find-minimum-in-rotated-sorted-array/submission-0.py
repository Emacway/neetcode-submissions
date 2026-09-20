class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        n = len(nums)
        l = 0
        r = n - 1
        res = nums[0]

        while (l <= r):
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = l + ((r - l) // 2)
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]: #go right
                l = mid + 1
            else: # go left
                r = mid - 1
        return res



