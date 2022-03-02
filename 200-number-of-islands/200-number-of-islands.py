class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid) - 1
        column = len(grid[0]) - 1
        neigh = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0
        def dfs(i,j):
            nonlocal row, column, neigh
            if i < 0 or i > row or j < 0 or j > column or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for r, c in neigh:
                dfs(i+r,j+c)
        for r in range(row + 1):
            for c in range(column + 1):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)
        return count