class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        max_area = 0

        def area_of_island(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return 1 + area_of_island(r + 1, c) + area_of_island(r - 1, c) + area_of_island(r, c + 1) + area_of_island(r, c - 1)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    contender = area_of_island(r,c)

                    max_area = max(contender, max_area)

        return max_area
