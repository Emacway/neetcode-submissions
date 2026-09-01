class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)):
            if i != len(arr) - 1: # if not last index
                rightSide = arr[i+1:]
                ans.append(max(rightSide))
            else:
                ans.append(-1)
        return ans
