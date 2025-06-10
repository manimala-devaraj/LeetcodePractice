class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=map(lambda l:l**2,nums)
        l=list(res)
        l.sort()
        return l