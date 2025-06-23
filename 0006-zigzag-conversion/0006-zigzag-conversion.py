class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ['' for _ in range(numRows)]
        new= 0
        con= False

        for i in s:
            rows[new] += i

            if new== 0 or new== numRows - 1:
                con= not con
            new+= 1 if con else -1

        return ''.join(rows)
