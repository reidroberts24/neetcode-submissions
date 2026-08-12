class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}
        for i, n in enumerate(nums):
            target_difference = target - n
            if target_difference in difference_map:
                return [difference_map[target_difference],i]
            difference_map[n] = i