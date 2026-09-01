class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n # products of vals to the LEFT of index i
        suff = [0] * n # products of vals to the RIGHT of index i
        res = [0] * n # result

        pref[0] = 1 # first index has nothing to the left
        suff[n - 1] = 1 # last index has nothing to the right
        
        # build the prefix array
        for i in range(1, n):
            #previous number times previous product (left to right)
            pref[i] = (pref[i - 1] * nums[i - 1]) 
        
        # build the suffix array
        for i in range(n - 2, -1, -1):
            #next number times next product (right to left)
            suff[i] = (suff[i + 1] * nums[i + 1]) 
        
        

        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res
