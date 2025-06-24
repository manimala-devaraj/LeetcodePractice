class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        be=nums[0]
        curr=0
        for i in nums:
            curr=max(i, curr+i)
            be=max(be,curr)
        return be