class Solution:
    def fib(self, n: int) -> int:
        # a,b=0,1
        # for i in range(n):
        #     a,b=b,a+b
        # return a
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


