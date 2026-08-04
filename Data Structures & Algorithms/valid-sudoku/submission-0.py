class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            I: 2x2 matrix of board
            O: if its a sudoku
            C: fixed length of board, values are 1-9 or .
            E: there might not be a valid item in the board potentially

            sets keep track of duplicates (if duplicate then no good)

            Three rules:
                1: rows check
                2: columns check
                3: square check

            Split question into a bunch of O(N) searches
            - Search all rows ()
            - Search all columns
            - Search the 9 squares

            It may be possible to do each of them at the same time, for understanding sake I'm going to do each one by one.
        '''


        # checking rows

        for irow in range(len(board)):
            my_set = set()

            for icol in range(len(board[0])):
                if board[irow][icol] == ".":
                    continue
                
                if board[irow][icol] in my_set:
                    return False

                my_set.add(board[irow][icol])
        
        # checking columns

        for icol in range(len(board[0])):
            my_set = set()
            for irow in range(len(board)):
                if board[irow][icol] == ".":
                    continue
                
                if board[irow][icol] in my_set:
                    return False

                my_set.add(board[irow][icol])

        # checking individual 3x3 subarrays
        for i_start in range(0, 7, 3):
            for j_start in range(0, 7, 3):
                my_set = set()
                for i in range(i_start, i_start + 3):
                    for j in range(j_start, j_start + 3):
                        if board[i][j] == ".":
                            continue
                        
                        if board[i][j] in my_set:
                            return False

                        my_set.add(board[i][j])
        return True