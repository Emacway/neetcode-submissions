class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n) approach
        maxArea = 0
        area = 0

        # if heights is empty, return 0
        if heights == []:
            return 0

        # initialize two pointers
        i = 0 #left side
        j = len(heights) - 1 #right side

        
        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width
            if area > maxArea:
                maxArea = area
            # to update the two pointers, we move the pointer for the smaller height
            # if heights[i] is the height, this is the max area with that bar 
                # since this is the maximum width. same for heights[j]
            if height == heights[i]:
                i += 1
            if height == heights[j]:
                j -= 1

        return maxArea