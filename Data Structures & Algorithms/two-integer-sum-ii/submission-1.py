class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return 1-indexed pair of indices that add to target
        # index 1 cannot equal index 2

        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum > target:
                r -= 1
                continue
            elif cur_sum < target:
                l += 1
                continue
            else:
                return [l + 1, r + 1]
            