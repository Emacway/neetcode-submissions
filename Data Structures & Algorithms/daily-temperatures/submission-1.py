class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n) solution with a stack
        n = len(temperatures)

        if n == 1:
            return [0]
        
        result = [0] * n

        stack = [(0, temperatures[0])] # stores tuples of indeces and temperatures

        for i in range(n):
            today = temperatures[i]
            while stack != [] and today > stack[-1][1]:
                prevDay = stack.pop()
                index = prevDay[0]
                result[index] = i - index
            stack.append((i, today))

        return result
            
