class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi=cur=sum(nums[:k])
        for j in range(k,len(nums)):
            cur+=nums[j]-nums[j-k]
            maxi= max(maxi,cur)
        return maxi/k