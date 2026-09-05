class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #bitmask method
        rows = [0] * 9 # rows[i] stores bits for digits seen in row i
        cols = [0] * 9 # cols[i] stores bits for digits seen in column i
        squares = [0] * 9 # squares[i] stores bits for digits seen in 3x3 box i

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": #skip over the dots
                    continue

                val = int(board[r][c]) - 1 #consider 0 through 8 bit index

                mask = 1 << val #shift left val amount

                #if val is 5, mask is 00010000
                if mask & rows[r]:
                    return False
                if mask & cols[c]:
                    return False
                if mask & squares[(r // 3) * 3 + (c // 3)]:
                    return False

                # add to tracker
                rows[r] |= mask
                cols[c] |= mask
                squares[(r // 3) * 3 + (c // 3)] |= mask

        return True
