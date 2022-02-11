class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid,i,j)
        return count
    
    def dfs(self,grid,rows, columns):
        if rows < 0 or columns < 0 or rows >= len(grid) or columns >= len(grid[0]) or grid[rows][columns] == "0":
            return
        else:
            grid[rows][columns] = "0"
            self.dfs(grid, rows - 1, columns)
            self.dfs(grid, rows + 1, columns)
            self.dfs(grid, rows, columns -1)
            self.dfs(grid, rows, columns + 1)
            
            

    