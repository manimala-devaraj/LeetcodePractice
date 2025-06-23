class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r, c = len(mat), len(mat[0])
        result = []
        for d in range(r + c - 1):
            immat= []

            if d < c:
                row = 0
                col = d
            else:
                row = d - c + 1
                col = c - 1
            while row < r and col >= 0:
                immat.append(mat[row][col])
                row += 1
                col -= 1
            if d % 2 == 0:
                result.extend(immat[::-1])
            else:
                result.extend(immat)

        return result

    