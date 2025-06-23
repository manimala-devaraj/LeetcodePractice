class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        val= {}  
        sublen= 0
        start = 0  
        for i in range(len(s)):
            if s[i] in val and val[s[i]] >= start:
                start = val[s[i]] + 1
            val[s[i]] = i
            sublen = max(sublen, i - start + 1)

        return sublen
