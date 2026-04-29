class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def dfs(i, curSum):
            if curSum == 0:
                res.append(combination.copy())
                return
            if i >= len(nums) or curSum < 0:
                return
            combination.append(nums[i])
            dfs(i, curSum - nums[i])
            combination.pop()
            dfs(i + 1, curSum)
        
        dfs(0, target)
        return res