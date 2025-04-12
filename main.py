# A function to check checkmate
# A function to check if a piece killed

# Next Step: function for check and checkmate

pieces = {
'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',  #for white 
'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',  #for black
'.': '·'
}


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


def displayBoard(board):
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
    

def move(board,src,dest):
    iSrc,jSrc = convertLocation(src)
    iDest,jDest = convertLocation(dest)
    toPlace = board[iSrc][jSrc]
    
    #check which piece is on the source, then send the src and destination in the checkValid function of that piece
    # print("To place: ", toPlace)
    valid = False
    
    # if opponentOrOwnPiece(board,src,dest):
    #     if toPlace == 'p':
    #         valid = validMovePawn(src,dest)
    #     elif toPlace == 'r':
    #         valid = validMoveRook(src,dest)
    #     elif toPlace == 'n':
    #         valid = validMoveKnight(src,dest)
    #     elif toPlace == 'b':
    #         valid = validMoveBishop(src,dest)
    #     elif toPlace == 'q':
    #         valid = validMoveQueen(src,dest)
    #     elif toPlace == 'k':
    #         valid = validMoveKing(src,dest)
    #     elif toPlace == '.':
    #         valid = False


    # Just for now to run both oponent and me manually
    if toPlace == 'p':
        valid = validMovePawn(board,src,dest)
    if toPlace == 'P':
        valid = opponentValidMovePawn(board,src,dest)
    elif toPlace == 'r' or toPlace == 'R':
        valid = validMoveRook(board,src,dest)
    elif toPlace == 'n' or toPlace == 'N':
        valid = validMoveKnight(src,dest)
    elif toPlace == 'b' or toPlace == 'B':
        valid = validMoveBishop(board,src,dest)
    elif toPlace == 'q' or toPlace == 'Q':
        valid = validMoveQueen(src,dest)
    elif toPlace == 'k' or toPlace == 'K':
        valid = validMoveKing(src,dest)
    elif toPlace == '.':
        valid = False
    
    if valid:
        board[iSrc][jSrc] = '.'
        board[iDest][jDest] = toPlace
    else:
        print("invalid move")
        return

def opponentOrOwnPiece(board,src,dest):
    ownPieces =  ['r', 'n', 'b', 'q', 'k', 'p']
    iDest, jDest = convertLocation(dest)
    pieceOnDest = board[iDest][jDest]
    
    if pieceOnDest in ownPieces:
        return False
    else:
        return True 

def validMovePawn(board,src,dest):
    #Problem: if opponent piece in next place, then cant move
    opponentPieces =  ['R', 'N', 'B', 'Q', 'K', 'P']
    iSrc,jSrc = convertLocation(src)
    iDest, jDest = convertLocation(dest)
    moves = iSrc - iDest
    
    diagnol1 = board[iSrc-1][jSrc-1]
    diagnol2 = board[iSrc-1][jSrc+1]
    
    if jSrc == jDest and moves > 0:
        if board[iSrc-1][jSrc] == '.':    
            if moves == 1:
                return True
            elif moves == 2 and iSrc == 6 :
                return True
            else:
                return False
    elif diagnol1 in opponentPieces and iDest == iSrc - 1 and jDest == jSrc - 1:
        print(diagnol1)
        return True
    elif diagnol2 in opponentPieces and iDest == iSrc - 1 and jDest == jSrc + 1:
        print(diagnol2)
        return True
    else:
        return False
    
def opponentValidMovePawn(board,src,dest):
    #Problem: if opponent piece in next place, then cant move
    opponentPieces =  ['r', 'n', 'b', 'q', 'k', 'p']
    iSrc,jSrc = convertLocation(src)
    iDest, jDest = convertLocation(dest)
    moves = iDest - iSrc
    
    diagnol1 = board[iSrc+1][jSrc-1]
    diagnol2 = board[iSrc+1][jSrc+1]
    
    if jSrc == jDest and moves > 0:
        if board[iSrc+1][jSrc] == '.':    
            if moves == 1:
                return True
            elif moves == 2 and iSrc == 1 :
                return True
            else:
                return False
    elif diagnol1 in opponentPieces and iDest == iSrc + 1 and jDest == jSrc - 1:
        print(diagnol1)
        return True
    elif diagnol2 in opponentPieces and iDest == iSrc + 1 and jDest == jSrc + 1:
        print(diagnol2)
        return True
    else:
        return False

def validMoveRook(board,src,dest):
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
                valid = False
                
    #horizontally              
    elif iSrc == iDest:
        if jDest > jSrc:
            step = 1
        else:
            step = -1
        for j in range(jSrc+step, jDest, step):
            if board[iSrc][j] != '.':
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

def validMoveBishop(board,src,dest):
    iSrc,jSrc = convertLocation(src)
    iDest,jDest = convertLocation(dest)
    iStep = iSrc
    jStep = jSrc
    valid = True
    moves = 0
    iMoves = 0
    jMoves = 0
    if(iDest > iSrc):
        moves = iDest - iSrc
        iMoves = iDest - iSrc
    else:
        moves = iSrc- iDest
        iMoves = iSrc- iDest
        
    if(jDest > jSrc):
        jMoves = jDest - jSrc
    else:
        jMoves = jSrc- jDest
    
    
    if iMoves == jMoves:
        # Down Right
        if iDest > iSrc and jDest > jSrc:
            print("Down Right")
            for i in range(moves-1):
                iStep += 1
                jStep += 1
                if board[iStep][jStep] != '.':
                    valid = False
        # Up Right
        elif iDest < iSrc and jDest > jSrc:
            print("Up Right")
            for i in range(moves-1):
                iStep -= 1
                jStep += 1
                if board[iStep][jStep] != '.':
                    print("False at i: ",iStep," j: ",jStep)
                    valid = False
        # Down Left
        elif iDest > iSrc and jDest < jSrc:
            print("Down Left")
            for i in range(moves-1):
                iStep += 1
                jStep -= 1
                if board[iStep][jStep] != '.':
                    valid = False
        # Up Left
        elif iDest < iSrc and jDest < jSrc:
            print("Up Left")
            for i in range(moves-1):
                iStep -= 1
                jStep -= 1
                if board[iStep][jStep] != '.':
                    valid = False
    else:
        valid = False
        
    return valid

def validMoveQueen(src,dest):
    if validMoveBishop(src,dest):
        return True
    elif validMoveRook(src,dest):
        return True
    else:
        return False

def validMoveKing(src,dest):
    iSrc,jSrc = convertLocation(src)
    iDest,jDest = convertLocation(dest)
    
    if iDest == iSrc-1 and jDest == jSrc:
        return True
    elif iDest == iSrc-1 and jDest == jSrc+1:
        return True
    elif iDest == iSrc and jDest == jSrc+1:
        return True
    elif iDest == iSrc+1 and jDest == jSrc+1:
        return True
    elif iDest == iSrc+1 and jDest == jSrc:
        return True
    elif iDest == iSrc+1 and jDest == jSrc-1:
        return True
    elif iDest == iSrc and jDest == jSrc-1:
        return True
    elif iDest == iSrc-1 and jDest == jSrc-1:
        return True
    else:
        return False
    

def main():

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
    while True:
        # display_board(board)
        src,dest = moveUserInput()
        move(board,src,dest)
        display_board(board)


main()