class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        max_l = [0] * len(height)
        max_r = [0] * len(height)
        
        for i in range(len(height)):
            j = -i - 1
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
            max_l[i] = l_wall
            max_r[j] = r_wall
        
        res = 0
        for i in range(len(height)):
            cur = min(max_l[i], max_r[i]) - height[i]
            if cur <= 0:
                continue
            else:
                res += cur
        return res