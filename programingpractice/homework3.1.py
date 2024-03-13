
board =[[0,0,5,3,0,0,0,0,0],
        [8,0,0,0,0,0,0,2,0],
        [0,7,0,0,1,0,5,0,0],
        [4,0,0,0,0,5,3,0,0],
        [0,1,0,0,7,0,0,0,6],
        [0,0,3,2,0,0,0,8,0],
        [0,6,0,5,0,0,0,0,9],
        [0,0,4,0,0,0,0,3,0],
        [0,0,0,0,0,9,7,0,0]]


#part1
def valid_move(board, row, column, number):

    is_row = number not in board[row]
    
    is_column = number not in [i[column] for i in board]
    
    blk_column, blk_row = (column//3) * 3, (row//3) * 3
    blk_board = [i[blk_column:blk_column + 3] for i in board[blk_row:blk_row + 3]]
    is_block = number not in sum(blk_board, [])

    if board[row][column] != 0:
        is_already = False

    return all([is_row, is_column, is_block, is_already])


#part2

def find_empty_cell(board):
    
    for y in range(0,9):
        
        for x in range(0,9):
            
            if board[y][x] == 0:
                return y, x
            
    return -1,-1


def new_valid_move(board, row, column, number):

    is_row = number not in board[row]
    
    is_column = number not in [i[column] for i in board]
    
    blk_column, blk_row = (column//3) * 3, (row//3) * 3
    blk_board = [i[blk_column:blk_column + 3] for i in board[blk_row:blk_row + 3]]
    is_block = number not in sum(blk_board, [])

    return all([is_row, is_column, is_block])


def solve_sudoku(board):
    
    y,x = find_empty_cell(board)
    
    if y == -1 or x == -1:
        return True

    for value in range(1,10):
        if new_valid_move(board, y , x, value):
            board[y][x] = value

            if solve_sudoku(board):
                return True
            
            board[y][x] = 0
            
    return False


solve_sudoku(board)
[print(i) for i in board]


