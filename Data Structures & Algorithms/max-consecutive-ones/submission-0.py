class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        cur_count = 0
        for n in nums:
            if n == 1:
                cur_count += 1
                max_count = max(max_count, cur_count)
                continue
            cur_count = 0
        return max_count