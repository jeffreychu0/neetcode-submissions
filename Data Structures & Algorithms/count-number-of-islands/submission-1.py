class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0

        movements = [(1,0), (0,1), (-1,0), (0,-1)]

        def explore_island(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for vert, hor in movements:
                explore_island(r + vert, c + hor)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    explore_island(r,c)
                    islands += 1
        
        return islands