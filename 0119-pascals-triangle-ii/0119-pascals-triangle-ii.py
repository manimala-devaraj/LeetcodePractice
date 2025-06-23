class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        mat= []

        for i in range(rowIndex+1):
            row = [1] * (i + 1)  
            for j in range(1, i):
                row[j] = mat[i-1][j-1] + mat[i-1][j]
            mat.append(row)
        return mat[rowIndex]
        
