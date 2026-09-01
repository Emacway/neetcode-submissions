class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums  = []
        for i, num in enumerate(nums):
            sortedNums.append([num, i])
        sortedNums.sort()

        i = 0 #first index
        j = len(nums) - 1 # last index

        while i < j:
            if sortedNums[i][0] + sortedNums[j][0] == target:
                return [min(sortedNums[i][1],sortedNums[j][1]),
                max(sortedNums[i][1],sortedNums[j][1])]
            elif sortedNums[i][0] + sortedNums[j][0] < target:
                i += 1
            elif sortedNums[i][0] + sortedNums[j][0] > target:
                j -= 1
        return []
        
