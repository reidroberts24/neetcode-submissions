class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                height, index = stack.pop()
                largest = max(largest, height * (i - index))
                start = index
            stack.append((h, start))
        
        for h, i in stack:
            largest = max(largest, h * (len(heights) - i))
        
        return largest