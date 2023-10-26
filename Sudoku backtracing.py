board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]==0:
                return row,col 
            
# i have 3 rules , the col, the row , the square            
def ValidPlacement(board,row, col,number):
    for i in range(9):
        if board[row][i] == number and col !=i:
            return False 
        # we check that the whole row dosen't contain
        # the value that we just inserted, and we skip
        # our position , make sense ya3ny
    for i in range (9):
        if board[i][col] == number and row !=i:
            return False 
        #check for the column
    
    #and then check for the square
    #it has 6 squares , 3 rows and 3 cols
    # 0,1,2 rows and 0,1,2 cols 
    # so to check which square we gonna devide //3

    square_row_i = row //3
    square_col_i = col//3

    # what is the realtion between the index of the row and it's elements
    # row is in range square_row_i*3 to square_row_i*3 + 2 (try it with your hands)
    #oops i found that the column is the same 🙈

    for s_row in range (square_row_i*3,square_row_i*3 + 3):
        for s_col in range (square_col_i*3 , square_col_i*3 + 3):
            if board[s_row][s_col] == number and (s_col!=col and s_row !=row):
                return False 
    # if you went through all of these loops and you didn't return false 
    #so it's a vaild position
    return True 
def solve(row, col):
    if col == board[row].length:

    for i in range(1,10):
        board[row][col]= i
        if(ValidPlacement(row,col)): 
            if(solve(row,col+1,board)):
                return True;
