class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        w= sentence.split()  
        for i in range(len(w)):
            if w[i].startswith(searchWord):
                return i + 1  
        else:
            return -1
