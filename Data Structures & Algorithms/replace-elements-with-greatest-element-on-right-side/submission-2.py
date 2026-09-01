class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        for i in range(n):
            rightMax = -1
            for j in range(i+1, len(arr)):
                if arr[j] > rightMax:
                    rightMax = arr[j]
            ans[i] = rightMax
        return ans
