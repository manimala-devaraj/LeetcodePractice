class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        t=0
        count=Counter(chars)  
        for i in words:
            s=Counter(i)
            if all(s[c] <=count.get(c, 0) for c in i):
                t+=len(i)
        return t
