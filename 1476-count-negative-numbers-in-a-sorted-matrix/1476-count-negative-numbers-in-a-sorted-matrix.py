class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        p=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    p.append(grid[i][j])
        return len(p)