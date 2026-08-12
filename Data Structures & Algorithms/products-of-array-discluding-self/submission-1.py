class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) in {0, 1}:
            return nums
        prefix, postfix = nums[:], nums[:]
        for i in range(1, len(nums) - 1):
            j = len(nums) - i - 1
            prefix[i] *= prefix[i - 1]
            postfix[j] *= postfix[j + 1]

        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * postfix[i + 1]
        return res
