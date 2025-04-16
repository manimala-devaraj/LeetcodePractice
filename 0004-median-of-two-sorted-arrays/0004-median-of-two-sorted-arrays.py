class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k=sorted(nums1+nums2)
        l=len(k)
        if l%2==1:
            m=(k[l//2])
            return m
        else:
            n= (k[l//2-1]+k[l//2])/2
            return n
    

        