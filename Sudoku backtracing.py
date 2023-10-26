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



def solve(row, col):
    if col == board[row].length:

    for i in range(1,10):
        board[row][col]= i
        if(ValidPlacement(row,col)): 
            if(solve(row,col+1,board)):
                return True;
