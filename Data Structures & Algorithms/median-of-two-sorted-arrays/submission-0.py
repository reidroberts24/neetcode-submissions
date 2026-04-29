class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = sorted(nums1 + nums2)
        L = len(new)
        print(new)
        if L % 2 == 0:
            m1 = new[L // 2 - 1]
            m2 = new[L // 2]
            return (m1 + m2) / 2
        else:
            return new[L // 2]
        
            

