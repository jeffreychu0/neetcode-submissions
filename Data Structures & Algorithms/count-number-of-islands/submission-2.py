class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        # this is a problem to count the max sub areas of 1. 

        # lets say we iterate through the entire grid. Then we can confirm whether or not we find 1's that are or are not ocnnected.

        # as we iterate through i, j, keep visited set and search through the entire island 

        visited = set()

        def explore_island(i, j):
            if (i,j) in visited or i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] == "0":
                return
            
            visited.add((i,j))
            explore_places = [(0,1), (1,0), (0,-1), (-1,0)]

            for i_diff, j_diff in explore_places:
                explore_island(i + i_diff, j + j_diff)
            
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += 1
                    explore_island(i,j)

        return count