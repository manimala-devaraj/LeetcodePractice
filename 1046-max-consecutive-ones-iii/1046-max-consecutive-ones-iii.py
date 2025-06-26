class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        maxilen=0
        zcnt=0
        for i in range(len(nums)):
            if nums[i] == 0:
                zcnt+= 1

            while zcnt> k:
                if nums[left] == 0:
                    zcnt-= 1
                left += 1
            ma=i-left + 1
            maxilen = max(maxilen,ma)
        return maxilen