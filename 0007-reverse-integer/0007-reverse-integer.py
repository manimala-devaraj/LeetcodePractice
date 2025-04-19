class Solution:
    def reverse(self, x: int) -> int:
        ino=(-2**31)
        esx=(2**31-1)
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
            rem= (-rem)
        if rem<ino or rem>esx:
            return 0
        return rem



        