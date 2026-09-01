class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        zero_cnt = 0
        prod = 1
        for i in range(n):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return res
        elif zero_cnt == 1:
            for i in range(n):
                if nums[i] == 0:
                    res[i] = prod
            return res
        else: 
            for i in range(n):
                res[i] = prod // nums[i]
            return res