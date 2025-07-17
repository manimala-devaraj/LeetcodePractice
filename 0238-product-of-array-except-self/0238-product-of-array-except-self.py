class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s=len(nums)
        res=[0]*s
        su=1
        for i in range(s):
            res[i]=su
            su*=nums[i]
        ri=1
        for i in range(s-1,-1,-1):
            res[i]*=ri
            ri*=nums[i]
        return res

    