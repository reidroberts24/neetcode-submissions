class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        for n in nums:
            if n not in numset:
                return True
            numset.remove(n)
        return False