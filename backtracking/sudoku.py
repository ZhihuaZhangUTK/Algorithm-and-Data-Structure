def solveSudoku(board):
    row, col = findUnassigned(board)
    #no unassigned position is found, puzzle solved
    if row == -1 and col == -1:
        return True
    for num in ["1","2","3","4","5","6","7","8","9"]:
        if isSafe(board, row, col, num):
            board[row][col] = num
            if solveSudoku(board):
                return True
            board[row][col] = "."
    return False

def findUnassigned(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                return row, col
    return -1, -1
           
def isSafe(board, row, col, ch):
    boxrow = row - row%3
    boxcol = col - col%3
    if checkrow(board, row,ch) and checkcol(board,col,ch) and checksquare(board,boxrow, boxcol, ch):
        return True
    return False

def checkrow(board, row, ch):
    for col in range(9):
        if board[row][col] == ch:
            return False
    return True

def checkcol(board, col, ch):
    for row in range(9):
        if board[row][col] == ch:
            return False
    return True
   
def checksquare(board, row, col, ch):
    for r in range(row, row+3):
        for c in range(col, col+3):
            if board[r][c] == ch:
                return False
    return True

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

solveSudoku(board)
print(board)
