class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1) :
                    self.dfs(grid,i,j)
        self.replace(grid, "O", "X")
        self.replace(grid, "A", "O")
    def replace(self, grid, char1, char2):
        for i in grid:
            for j in range(len(grid[0])):
                if i[j] == char1:
                    i[j] = char2
        
    def dfs(self,grid,rows, columns):
        if rows < 0 or columns < 0 or rows >= len(grid) or columns >= len(grid[0]) or grid[rows][columns] == "X" or grid[rows][columns]=="A":
            return
        else:
            grid[rows][columns] = "A"
            self.dfs(grid, rows - 1, columns)
            self.dfs(grid, rows + 1, columns)
            self.dfs(grid, rows, columns -1)
            self.dfs(grid, rows, columns + 1)
        
            