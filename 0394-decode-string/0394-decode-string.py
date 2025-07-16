class Solution:
    def decodeString(self, s: str) -> str:
        sa=[]
        c=''
        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=='[':
                sa.append((c,num))
                c=''
                num=0
            elif i==']':
                pr,ti=sa.pop()
                c=pr+c*ti
            else:
                c+=i
        return c
