class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        while n>=5:
            n//=5
            count+=n
        return count
        #count=0 
        #mul=1
        # for i in range(1,n+1):
        #     mul*=i
        #     pass
            
        # for j in (str(mul)[::-1]):
        #     if j=='0':
        #         count+=1
        #     else:
        #         break
        # return count
        