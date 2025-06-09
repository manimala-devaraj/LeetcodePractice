class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        k=0
        for i in nums:
            if c== 0:
                k=i
            c+= (1 if i == k else -1)

        return k


        
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       