class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
            numToIndex[num] = i
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numToIndex and numToIndex[complement] != i:
                return [i, numToIndex[complement]]

