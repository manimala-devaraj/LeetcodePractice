class Solution:
    def trailingZeroes(self, n: int) -> int:
        # count=0
        # while n>=5:
        #     n//=5
        #     count+=n
        # return count
        if n < 5:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)