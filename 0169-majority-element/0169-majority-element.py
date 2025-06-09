class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        c=nums[n//2]
        return c
        # cnt=0
        # k=0
        # for i in nums:
        #     if cnt== 0:
        #         k=i
        #     cnt+=(1 if i == k else -1)
        # return k


        
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       