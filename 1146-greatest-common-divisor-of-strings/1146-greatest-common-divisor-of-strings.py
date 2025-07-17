class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd=str1  if len(str1)<len(str2) else str2

        def isdivi(word,div):
            s,m=len(div),len(word)
            if m%s!=0:
                return False
            j=0
            for i in range(m):
                if word[i]!=div[j]:
                    return False
                j=(j+1)%s
            return True
        while len(gcd)>0:
            if isdivi(str1,gcd) and isdivi(str2,gcd):
                return gcd
            gcd=gcd[:-1]
        return ''