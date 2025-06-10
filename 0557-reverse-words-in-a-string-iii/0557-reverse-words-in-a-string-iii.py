class Solution:
    def reverseWords(self, s: str) -> str:
        n=s.split()
        res=map(lambda l:l[::-1],n)
        p=" ".join(res)
        return p
        