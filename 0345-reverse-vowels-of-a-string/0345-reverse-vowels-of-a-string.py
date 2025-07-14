class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i in s if i in 'aeiouAEIOU']  
        result = []
        for i in s:
            if i in 'aeiouAEIOU':
                result.append(vowels.pop())  
            else:
                result.append(i) 
        return ''.join(result)