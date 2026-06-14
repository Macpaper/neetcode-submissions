class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # start = grid[0][0]
        # end = grid[-1][-1]
        cols = len(grid[0])
        rows = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        prev = [[-1 for _ in range(cols)] for _ in range(rows)]  # <-- maybe needed to keep track of path idk how to do

        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        frontier = [(0, (0, 0))]
        dist[0][0] = 0

        while frontier:
            curr_dist, curr_node = heapq.heappop(frontier)
            r, c = curr_node

            if dist[r][c] < curr_dist:
                continue

            for dr, dc in dirs:
                next_r = dr + r
                next_c = dc + c
                if 0 <= next_r < rows and 0 <= next_c < cols:
                    nextDist = grid[next_r][next_c]
                    
                    if nextDist < dist[next_r][next_c]:
                        #THHIS WAS THE BIG THING I CHANGED IDK EXACTLY WHY IT WORKS
                        dist[next_r][next_c] = nextDist
                        heapq.heappush(frontier, (nextDist, (next_r, next_c)))
                        prev[next_r][next_c] = (r, c)

        curr = prev[-1][-1]
        largest = grid[-1][-1]
        while curr != -1:
            nr, nc = curr
            if grid[nr][nc] > largest:
                largest = grid[nr][nc]
            curr = prev[nr][nc]
        return largest