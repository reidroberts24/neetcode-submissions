class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, n in enumerate(nums):
            if n in hashmap:
                min_i = min(hashmap[n], i)
                max_i = max(hashmap[n], i)
                return [min_i, max_i]
            hashmap[target - n] = i
