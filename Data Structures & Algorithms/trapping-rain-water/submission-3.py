class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r] 
        total_vol = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                total_vol += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total_vol += rightMax - height[r]
        return total_vol
