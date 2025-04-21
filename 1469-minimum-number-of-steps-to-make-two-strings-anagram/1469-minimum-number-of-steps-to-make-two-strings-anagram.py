class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26  
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for ch in t:
            count[ord(ch) - ord('a')] -= 1
        steps = 0
        for val in count:
            if val > 0:
                steps += val
        return steps
        # cnt=0
        # for i in (s):
        #     if t in s:
        #         return cnt
        #     elif t not in s:
        #         cnt+=1
        #         return cnt


        