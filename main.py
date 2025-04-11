# A function to display chess board
# A function to check is valid move, for every chess piece different validation
# A function to check checkmate
# A function to check if a piece killed

pieces = {
'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',  #for white 
'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',  #for black
'.': '·'
}

board = [
    
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P','P','P','P','P','P','P','P'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['p','p','p','p','p','p','p','p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]

def display_board(board):
    print("   ┌" + "───┬" * 7 + "───┐")
    for i in range(8):
        row = f" {8 - i} │"
        for j in range(8):
            piece = pieces[board[i][j]]
            row += f"{piece.center(3)}│"
        print(row)
        if i < 7:
            print("   ├" + "───┼" * 7 + "───┤")
        else:
            print("   └" + "───┴" * 7 + "───┘")
    print("     a   b   c   d   e   f   g   h")


def displayBoard():
    print()
    for i in range(8):
        row = f"{8-i} "
        for j in range(8):
            row += pieces[board[i][j]] + " "
        print(row)
    print("  a b c d e f g h")
    print()

def moveUserInput():
    rows = ['a','b','c','d','e','f','g','h']
    cols = ['1','2','3','4','5','6','7','8']
    
    source = input("Enter the location(e.q e2,b5) of the piece you want to move: ")
    destination = input("Enter the location(e.q e2,b5) where you want to move the piece: ")
    
    while True:
        if source[0] not in rows or source[1] not in cols:
            source = input("Inavlid location, enter source again: ")
        elif destination[0] not in rows or destination[1] not in cols:
            destination = input("Inavlid location, enter destination again: ")
        else:
            break

    return source,destination

def convertLocation(loc):
    cols = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8'}
    row = 8 - int(loc[1])
    col = int(cols[loc[0]]) - 1
    
    return row,col
    

def move(src,dest):
    iSrc,jSrc = convertLocation(src)
    iDest,jDest = convertLocation(dest)
    toPlace = board[iSrc][jSrc]
    
    #check which piece is on the source, then send the src and destination in the checkValid function of that piece
    # print("To place: ", toPlace)
    valid = False
    
    if opponentOrOwnPiece(src,dest):
        if toPlace == 'p':
            valid = validMovePawn(src,dest)
        elif toPlace == 'r':
            valid = validMoveRook(src,dest)
        elif toPlace == 'n':
            valid = validMoveKnight(src,dest)
        elif toPlace == '.':
            valid = False

    
    if valid:
        board[iSrc][jSrc] = '.'
        board[iDest][jDest] = toPlace
    else:
        print("invalid move")
        return

def opponentOrOwnPiece(src,dest):
    ownPieces =  ['r', 'n', 'b', 'q', 'k', 'p']
    iDest, jDest = convertLocation(dest)
    pieceOnDest = board[iDest][jDest]
    
    if pieceOnDest in ownPieces:
        return False
    else:
        return True 

def validMovePawn(src,dest):
    opponentPieces =  ['R', 'N', 'B', 'Q', 'K', 'P']
    iSrc,jSrc = convertLocation(src)
    iDest, jDest = convertLocation(dest)
    moves = iSrc - iDest
    
    diagnol1 = board[iSrc-1][jSrc-1]
    diagnol2 = board[iSrc-1][jSrc+1]
    
    if jSrc == jDest and moves > 0:
        if moves == 1:
            return True
        elif moves == 2 and iSrc == 6 and board[iSrc-1][jSrc] == '.':
            print("Moves: ",moves)
            print("i source: ",iSrc)
            print("",board[iSrc-1][jSrc])
            return True
        else:
            return False
    elif diagnol1 in opponentPieces or diagnol2 in opponentPieces:
        if iDest == iSrc - 1 and jDest == jSrc - 1:
            return True
        elif iDest == iSrc - 1 and jDest == jSrc + 1:
            return True
        else:
            return False
    else:
        return False
        


def validMoveRook(src,dest):
    iSrc,jSrc = convertLocation(src)
    iDest, jDest = convertLocation(dest)
    valid = True

    #vertically
    if jSrc == jDest:  
        if iDest > iSrc:
            step = 1
        else:
            step = -1
        for i in range(iSrc+step, iDest,step):
            if board[i][jSrc] != '.':
                print("False at: ",board[i][jSrc])
                valid = False
                
    #horizontally              
    elif iSrc == iDest:
        if jDest > jSrc:
            step = 1
        else:
            step = -1
        for j in range(jSrc+step, jDest, step):
            if board[iSrc][j] != '.':
                print("Blocking at: ",board[iSrc][j])
                valid = False
    else:
        valid = False
    
    return valid
        
def validMoveKnight(src,dest):
    iSrc,jSrc = convertLocation(src)
    iDest,jDest = convertLocation(dest)
    
    if iDest == iSrc-2 and jDest == jSrc-1:
        return True
    elif iDest == iSrc-2 and jDest == jSrc+1:
        return True
    elif iDest == iSrc+2 and jDest == jSrc-1:
        return True
    elif iDest == iSrc+2 and jDest == jSrc+1:
        return True
    elif iDest == iSrc-1 and jDest == jSrc-2:
        return True
    elif iDest == iSrc-1 and jDest == jSrc+2:
        return True
    elif iDest == iSrc+1 and jDest == jSrc-2:
        return True
    elif iDest == iSrc+1 and jDest == jSrc+2:
        return True
    else:
        return False

def main():
    while True:
        # display_board(board)
        src,dest = moveUserInput()
        move(src,dest)
        display_board(board)


main()