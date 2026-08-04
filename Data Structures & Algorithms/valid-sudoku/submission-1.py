class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[row])):
                square = (row // 3, col // 3)

                if board[row][col] == ".":
                    continue

                val = board[row][col]

                if val in rows[row]:
                    return False
                if val in cols[col]:
                    return False
                if val in squares[square]:
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                squares[square].add(val)

        return True