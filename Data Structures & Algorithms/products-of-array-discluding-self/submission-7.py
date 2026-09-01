class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Optimal solution!!
        n = len(nums)
        res = [1] * n # initialize result array
        prefix = 1
        for i in range(n):
            res[i] = prefix #prefix is product of elements to the LEFT of i
            prefix *= nums[i] #update prefix before moving to next value
        postfix = 1 #postfix is product of elements to the RIGHT of i
        for i in range(n - 1, -1, -1): # going right to left second pass
            res[i] *= postfix #multiply by what is already in res[i]
            postfix *= nums[i] #update postfix before moving to next value
            

        return res

    
