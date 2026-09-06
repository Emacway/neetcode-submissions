class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            target = -nums[i]
            triplet = []
            # want to check pairs nums[j] and nums[k] so that 
            # nums[j] + nums[k] == -num1
            j = i + 1 #left
            k = len(nums) - 1 #right
            while j < k:
                if (nums[j] + nums[k]) < target:
                    j += 1
                elif (nums[j] + nums[k]) > target:
                    k -= 1
                if (nums[j] + nums[k]) == target and j != k:
                    triplet.append(-target)
                    triplet.append(nums[j])
                    triplet.append(nums[k])
                    triplet.sort()
                    if triplet not in res:
                        res.append(triplet)
                        triplet = []
                    else: 
                        triplet = []
                        j += 1
                    
        return res
