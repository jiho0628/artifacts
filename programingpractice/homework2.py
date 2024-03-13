import sys


board2 =[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

print('以下に数独の情報を入力してください。例)1 2 3 4 5 6 7 8 9')

board = [ list(map(int,input().split(" "))) for i in range(9)]

#valid or invalid
#board[縦][横]

#check the board
if len(board) != 9:
    print('縦の長さを間違えています')
    sys.exit()
for i in range(0,9):
    if len(board[i]) != 9:
        print('横の長さを間違えています')
        sys.exit()

for i in range(0,9):
    for j in range(0,9):
        if board[i][j] > 9 or board[i][j] < 0:
            print('0-9の値を入れてください')
            sys.exit()



#check the row of SUDOKU
def row_check(a):
    numrow = 0
    for i in range(0, 9):
        for j in range(0, 9):
            for k in range(0, 9):
                if j != k:
                    
                    if a[i][k] == a[i][j] and a[i][k] != 0:
                        
                        numrow = numrow + 1
                    
                    else:
                        
                        numrow = numrow + 0
                        
                else:
                    pass
    return numrow


#check the col of SUDOKU
def col_check(a):
    numcol = 0
    for i in range(0, 9):
        for j in range(0, 9):
            for k in range(0, 9):
                if j != k:
                    
                    if a[k][i] == a[j][i] and a[k][i] != 0:
                        
                        numcol = numcol + 1
                    
                    else:
                        
                        numcol = numcol + 0
                        
                else:
                    pass
    return numcol


#make the boxes of SUDOKU
def make_box(a,box):
    boxlist = []
    r = (box // 3)*3
    c = (box % 3)*3
    for i in range(c,c+3):
        for j in range(r,r+3):
            boxlist.append(a[i][j])
    return boxlist
            



#check the box of SUDOKU
def box_check(a):
    numbox = 0
    for i in range(0,9):
        for j in range(0,9):
            for k in range(0,9):
                if j != k:

                    if make_box(a,i)[j] == make_box(a,i)[k] and make_box(a,i)[k] !=0:
                        numbox = numbox + 1

                    else:
                        numbox = numbox + 0
                else:
                    pass
    return numbox

if box_check(board) !=0:
    print("box内に重複があります。")

if row_check(board) !=0:
    print("row内に重複があります。")

if col_check(board) !=0:
    print("col内に重複があります。")
    
if row_check(board) + col_check(board) + box_check(board) == 0:
    print('valid')
else:
    print('invalid')







