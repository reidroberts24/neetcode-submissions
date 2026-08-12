class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # the individual values should not be duplicate in results
        # indices cannot be repeated
        # set of valid tuples 
        # check if valid tuple in set

        # hashmap with value as key, index as value
        # two pointers, check if target difference in hashmap
        # if so, check if it was already added

        targets = {}
        # targets = {
        #     1: 4,
        #     0: 1,
        #     -1: 2,
        #     -2: 3,
        #     4: 5

        # }
        for i, n in enumerate(nums):
            targets[n] = i
        valid_triplets = []
        # valid_triplets= set([-1,-1,0], [-1,0,1])

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                target_diff = -(nums[i] + nums[j])
                if target_diff in targets and targets[target_diff] not in [i,j]:
                    triplet = sorted([nums[i], nums[j], target_diff])
                    if triplet not in valid_triplets:
                        valid_triplets.append(triplet)
        return list(valid_triplets)