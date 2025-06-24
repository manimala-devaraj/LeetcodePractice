class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mat= []

        for i in range(numRows):
            row = [1] * (i + 1)  
            for j in range(1, i):
                row[j] = mat[i-1][j-1] + mat[i-1][j]
            mat.append(row)

        return mat
