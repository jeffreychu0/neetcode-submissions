class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def rot_adjacent_oranges(i, j):
            if i != 0:
                update_rotten_orange(i-1,j)
            
            if j != 0:
                update_rotten_orange(i, j-1)

            if j != len(grid[0]) - 1:
                update_rotten_orange(i, j + 1)
            
            if i != len(grid) - 1:
                update_rotten_orange(i + 1, j)
        
        def update_rotten_orange(i, j):
            nonlocal num_oranges
            if grid[i][j] == 1:
                grid[i][j] = 2
                num_oranges -= 1
                oranges.append((i, j))

        num_oranges = 0
        oranges = deque()
        minutes = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    num_oranges += 1
                elif grid[i][j] == 2:
                    oranges.append((i,j))

        while oranges and num_oranges > 0:
            for i in range(len(oranges)):
                pos = oranges.popleft()
                rot_adjacent_oranges(pos[0], pos[1])
            
            minutes += 1

        return -1 if num_oranges != 0 else minutes
            