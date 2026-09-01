class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
                else:
                    j += 1
            i += 1

