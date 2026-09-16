class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Alternative O(n) solution - Dynamic programming
        n = len(temperatures)

        if n == 1:
            return [0]
        
        result = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    j = n
                    break
                else:
                    j += result[j]
            if j < n and temperatures[j] > temperatures[i]:
                result[i] = j - i

        return result
