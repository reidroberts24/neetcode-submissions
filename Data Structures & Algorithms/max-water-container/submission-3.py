class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_vol = 0
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            max_vol = max(max_vol, h * w)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_vol