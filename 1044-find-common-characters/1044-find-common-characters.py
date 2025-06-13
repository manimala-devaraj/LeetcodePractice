class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        com=list(words[0])
        for i in words[1:]:
            l=[]
            for j in com:
                if j in i:
                    l.append(j)
                    i=i.replace(j,'',1)
            com=l
        return com 