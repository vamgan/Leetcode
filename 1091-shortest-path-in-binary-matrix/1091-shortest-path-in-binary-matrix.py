class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        maxRows = len(grid) - 1
        maxCol = len(grid[0]) - 1
        if grid[0][0] != 0 or grid[maxRows][maxCol] != 0:
            return -1
        queue = collections.deque()
        move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        def getNeigh(row,col):
            possibleDirections = []
            for r, c in move:
                newR = row + r
                newC = col + c
                if newR < 0 or newR > maxRows or newC < 0 or newC > maxCol:
                    continue
                if grid[newR][newC] != 0:
                    continue
                possibleDirections.append((newR, newC))
            return possibleDirections
        
        queue.append((0,0))
        grid[0][0] = 1
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if row == maxRows and col == maxCol:
                return distance
            for r,c in getNeigh(row,col):
                grid[r][c] = distance + 1
                queue.append((r,c))
        return -1
            
        
        