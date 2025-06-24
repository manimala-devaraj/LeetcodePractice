class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Check substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

        # start=0
        # mas=1
        # for i in range(len(s)):
        #     left,right=i,i
        #     while left>=0 and right<len(s) and s[left]==s[right]:
        #         if (right-left+1)>mas:
        #             start=left
        #             mas=right-left+1
        #         left-=1
        #         right+=1
        #     left,right=i,i+1
        #     while left>=0 and right<len(s) and s[left]==s[right]:
        #         if (right-left+1)>mas:
        #             start=left
        #             mas=right-left+1
        #         left-=1
        #         right+=1
        # palind=s[start:start+mas]
        # k=[]
        # for i in s:
        #     if i in palind:
        #         k.append(i)
        # return len(k)
                
        