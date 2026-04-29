class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        if target > nums[-1]:
            return search(0, pivot - 1)
        else:
            return search(pivot, len(nums) - 1)