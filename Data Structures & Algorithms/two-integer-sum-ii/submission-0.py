class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted in ascending order
        # one valid solution
        # return 1-indexed solution
        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum == target:
                return [l + 1, r + 1]
            while cur_sum > target:
                r -= 1
                cur_sum = numbers[l] + numbers[r]
            while cur_sum < target:
                l += 1
                cur_sum = numbers[l] + numbers[r]
        

                