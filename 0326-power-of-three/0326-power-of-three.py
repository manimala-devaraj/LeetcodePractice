class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(32):
            if 3**i <= n:
                if 3**i ==n:
                    return True
            else:
                return False
        