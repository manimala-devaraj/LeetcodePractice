class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        k=0
        for i in nums:
            if cnt== 0:
                k=i
            cnt+=(1 if i == k else -1)
        return k


        
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       