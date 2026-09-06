class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        
        
        def setDistance(r, c):
            visited = set()
            q = deque()
            q.append((r, c))
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while q:
                start_r, start_c = q.popleft()
                if (start_r, start_c) in visited: continue
                visited.add((start_r, start_c))

                for r, c in dirs:
                    new_r, new_c = r + start_r, c + start_c
                    if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                        if grid[new_r][new_c] > 0:
                            new_dist = grid[start_r][start_c] + 1
                            if new_dist < grid[new_r][new_c]:
                                grid[new_r][new_c] = new_dist
                                q.append((new_r, new_c))



        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    setDistance(r, c)