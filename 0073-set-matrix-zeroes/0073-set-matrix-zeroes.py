class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rzero = set()
        czero = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rzero.add(i)
                    czero.add(j)
        for i in range(rows):
            for j in range(cols):
                if i in rzero or j in czero:
                    matrix[i][j] = 0
    
