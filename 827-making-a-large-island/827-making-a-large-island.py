class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        mapper = {}
        islandId = 2
        large = 0
        row = len(grid) - 1
        column = len(grid[0]) - 1
        neigh = [(1,0), (-1,0), (0,1), (0,-1)]
        def valid(i,j):
            nonlocal row, column
            if i < 0 or i > row or j < 0 or j > column:
                return False
            return True
        def dfs(i,j, islandId, count):
            nonlocal neigh
            if not valid(i,j) or grid[i][j] != 1:
                return count
            grid[i][j] = islandId
            count += 1
            print(i,j)
            for r, c in neigh:
                count = dfs(i+r,j+c,islandId, count)
            return count
        for i in range(row + 1):
            for j in range(column + 1):
                count = 0
                if grid[i][j] == 1:
                    count = dfs(i,j, islandId, count)
                    mapper[islandId] = count
                    islandId += 1
        flag = False
        for i in range(row + 1):
            for j in range(column + 1):
                islandset = set()
                if grid[i][j] == 0:
                    flag = True
                    for r,c in neigh:
                        if valid(i + r, j + c) and grid[i + r][j+c] != 0:
                            islandset.add(grid[i + r][j+c])
                    total = 1
                    for id_ in islandset:
                        total += mapper[id_]
                    large = max(large, total)
        if not flag:
            return (row + 1) * (column + 1)
        return large