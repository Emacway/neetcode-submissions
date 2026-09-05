class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            if (self.hasDuplicates(row)):
                return False

        #check columns
        columns = []
        for i in range(9):
            column = []
            for row in board:
                column.append(row[i])
            columns.append(column)
        
        for column in columns:
            if self.hasDuplicates(column):
                return False
        

        #check sub boxes
        subBoxes = []
        for c in range(0,9,3):
            for r in range(0,9,3):
                box = []
                for i in range(r, r+3): #rows
                    for j in range(c, c+3): #columns
                        box.append(board[i][j])
                subBoxes.append(box)
        
        for box in subBoxes:
            if self.hasDuplicates(box):
                return False
        
        return True

    def hasDuplicates(self, item: List[str]) -> bool:
        digits = []
        for i in range(len(item)):
            if item[i].isdigit():
                digits.append(item[i])
        digitsSet = set(digits)
        return len(digitsSet) != len(digits)
        
        
        


