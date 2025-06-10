class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        mas=1
        for i in range(len(s)):
            left,right=i,i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1)>mas:
                    start=left
                    mas=right-left+1
                left-=1
                right+=1
            left,right=i,i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1)>mas:
                    start=left
                    mas=right-left+1
                left-=1
                right+=1
        palind=s[start:start+mas]
        return palind
        