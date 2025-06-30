class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        elif n==2:
            return "11"
        s="11"
        for i in range(n-2):
            val=''
            c=1
            for j in range(len(s)-1):
                if s[j]!=s[j+1]:
                    val+=str(c)+s[j]
                    c=1
                else:
                    c+=1
            else:
                val+=str(c)+s[j+1]
            s=val
        return s
