class Solution:
    def rob(self, nums: List[int]) -> int:
        p=[]
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        new = [0] * len(nums)
        new[0] = nums[0]
        new[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            new[i] = max(new[i-1], nums[i] + new[i-2])

        return new[-1]
