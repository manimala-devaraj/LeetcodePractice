class Solution:
    def climbStairs(self, n: int) -> int:
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2
        # fir=1
        # sec=2
        # for i in range(3,n+1):
        #     th=fir+sec
        #     fir=sec
        #     sec=th
        # return sec
        a=1
        b=1
        for i in range(n-1):
            a,b=a+b,a
        return a

        