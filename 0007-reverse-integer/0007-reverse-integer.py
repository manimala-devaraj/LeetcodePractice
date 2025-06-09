class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            rem=0
            while x!=0:
                rem=(rem*10)+(x%10)
                x//=10
        else:
            x=abs(x)
            rem=0
            while x!=0:
                rem=(rem*10)+(x%10)
                x//=10
            rem=(-rem)
        if (-2**31<=rem<=2**31-1):
            return rem
        else:
            return 0
    
        



    