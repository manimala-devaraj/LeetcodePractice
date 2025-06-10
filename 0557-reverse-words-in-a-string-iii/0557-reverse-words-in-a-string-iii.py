class Solution:
    def reverseWords(self, s: str) -> str:
        n=s.split()
        res=map(lambda l:l[::-1],n)
        p=" ".join(map(str,res))
        return p
        