class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        toVisit = deque()
        self.grid = grid

        visited = [[False] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    toVisit.append((row, col))
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # only visiting treasure chests first.
        steps = 0
        while toVisit:
            # each PASS THROUGH 
            steps += 1
            for _ in range(len(toVisit)):
                r, c = toVisit.popleft()
                visited[r][c] = True
                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c

                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] != -1 and visited[nr][nc] != True:
                        grid[nr][nc] = steps
                        visited[nr][nc] = True
                        toVisit.append((nr, nc))
        
    # def bfs(self, sr, sc):
    #     rows = self.rows
    #     cols = self.cols
    #     grid = self.grid
    #     q = deque()
    #     q.append((sr, sc))
    #     steps = 0
    #     while q:
    #         row, col = q.popleft()
    #         steps += 1
    #         for dr, dc in dirs:
    #             nr = dr + row
    #             nc = dc + col
    #             if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] > 0:
    #                 if grid[nr][nc] > steps:
    #                     grid[nr][nc] = steps
    #                     q.append((nr, nc))


