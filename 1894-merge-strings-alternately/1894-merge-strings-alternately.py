class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=0
        merge=''
        s1=len(word1)
        m1=len(word2)
        while i<s1 and j<m1:
            merge+=word1[i]+word2[j]
            i+=1
            j+=1
        if i<len(word1):
            merge+=word1[i:]
        else:
            merge+=word2[j:]
        return merge