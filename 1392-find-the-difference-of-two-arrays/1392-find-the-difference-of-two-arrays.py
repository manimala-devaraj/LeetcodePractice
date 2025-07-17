class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1 = list(set(nums1) - set(nums2))
        arr2 = list(set(nums2) - set(nums1))
        return [arr1, arr2]