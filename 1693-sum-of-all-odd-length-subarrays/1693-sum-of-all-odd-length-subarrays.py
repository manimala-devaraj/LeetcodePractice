class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        cnt=0
        n=len(arr)
        for i in range(n):
            for j in range(i,n):
                sub=arr[i:j+1]
                if len(sub)%2==1:
                    cnt+=sum(sub)
        return cnt