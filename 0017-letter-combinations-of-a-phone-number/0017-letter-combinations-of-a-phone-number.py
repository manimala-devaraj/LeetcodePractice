class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def backtrack(com,nexti):
            if not nexti:
                res.append(com)
                return
            
            for letter in phone[nexti[0]]:
                backtrack(com + letter, nexti[1:])
        
        backtrack("", digits)
        return res