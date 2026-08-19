class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()

        islands = 0

        movements = [(1,0), (0,1), (-1,0), (0,-1)]

        def explore_island(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return

            if grid[r][c] == "0" or (r,c) in visit:
                return
            
            visit.add((r,c))
            for vert, hor in movements:
                explore_island(r + vert, c + hor)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands += 1
                    explore_island(r,c)
        
        return islands