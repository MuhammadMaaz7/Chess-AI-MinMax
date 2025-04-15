# A function to check checkmate
# A function to check if a piece killed

# Next Step: function for check and checkmate

pieces = {
'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',  #for white 
'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',  #for black
'.': '·'
}

playerCastlingDone = False
playerKingMoved = False
playerRook1Moved = False
playerRook2Moved = False

oppeonentCastlingDone = False
oppeonentKingMoved = False
oppeonentRook1Moved = False
oppeonentRook2Moved = False

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

def moveUserInput(board,player):
    rows = ['a','b','c','d','e','f','g','h']
    cols = ['1','2','3','4','5','6','7','8']
    
    player1Pieces =  ['r', 'n', 'b', 'q', 'k', 'p']
    player2Pieces =  ['R', 'N', 'B', 'Q', 'K', 'P']
    
    source = input("Enter the location(e.q e2,b5) of the piece you want to move: ")
    destination = input("Enter the location(e.q e2,b5) where you want to move the piece: ")
    
    while True:
        iSrc,jSrc = convertLocation(source)
        iDest,jDest = convertLocation(destination)
        toMove = board[iSrc][jSrc]
    
        if source[0] not in rows or source[1] not in cols:
            source = input("Inavlid location, enter source again: ")
        elif destination[0] not in rows or destination[1] not in cols:
            destination = input("Inavlid location, enter destination again: ")
        elif player==1 and toMove in player2Pieces:
            source = input("Opponent piece selected, enter source again: ")
            destination = input("Enter destination again: ")
        elif player==2 and toMove in player1Pieces:
            source = input("Opponent piece selected, enter source again: ")
            destination = input("Enter destination again: ")
        else:
            break

    return source,destination

def convertLocation(loc):
    cols = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8'}
    row = 8 - int(loc[1])
    col = int(cols[loc[0]]) - 1
    
    return row,col

def indexToLocation(i, j):
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row = str(8 - i)
    col = cols[j]

    return col + row


def playerMove(board,src,dest):
    ownPieces =  ['r', 'n', 'b', 'q', 'k', 'p']
    opponentPieces = ['R', 'N', 'B', 'Q', 'K', 'P']
    iSrc,jSrc = convertLocation(src)
    iDest,jDest = convertLocation(dest)
    toPlace = board[iSrc][jSrc]
    
    valid = False
    
    checkCheck(board,src,opponentPieces)
    
    if opponentOrOwnPiece(board,src,dest,ownPieces):
        if toPlace == 'p':
            valid = validMovePawn(board,src,dest)
        elif toPlace == 'r':
            valid = validMoveRook(board,src,dest)
        elif toPlace == 'n':
            valid = validMoveKnight(src,dest)
        elif toPlace == 'b':
            valid = validMoveBishop(board,src,dest)
        elif toPlace == 'q':
            valid = validMoveQueen(board,src,dest)
        elif toPlace == 'k':
            valid = validMoveKing(board,src,dest)
        elif toPlace == '.':
            valid = False
        
    if valid == "castlingMove":
        return
    
    if valid:
        board[iSrc][jSrc] = '.'
        board[iDest][jDest] = toPlace
    else:
        print("invalid move")
        return
    
def opponentMove(board,src,dest):
    ownPieces =  ['R', 'N', 'B', 'Q', 'K', 'P']
    opponentPieces = ['r', 'n', 'b', 'q', 'k', 'p']
    iSrc,jSrc = convertLocation(src)
    iDest,jDest = convertLocation(dest)
    toPlace = board[iSrc][jSrc]
    
    valid = False
    
    checkCheck(board,src,opponentPieces)
    
    if opponentOrOwnPiece(board,src,dest,ownPieces):
        if toPlace == 'P':
            valid = opponentValidMovePawn(board,src,dest)
        elif toPlace == 'R':
            valid = validMoveRook(board,src,dest)
        elif toPlace == 'N':
            valid = validMoveKnight(src,dest)
        elif toPlace == 'B':
            valid = validMoveBishop(board,src,dest)
        elif toPlace == 'Q':
            valid = validMoveQueen(board,src,dest)
        elif toPlace == 'K':
            valid = validMoveKing(board,src,dest)
        elif toPlace == '.':
            valid = False
        
    if valid == "castlingMove":
        return
    
    if valid:
        board[iSrc][jSrc] = '.'
        board[iDest][jDest] = toPlace
    else:
        print("invalid move")
        return
    
def checkCheck(board,src,opponentPieces):
    iSrc,jSrc = convertLocation(src)
    
    if board[iSrc][jSrc] != 'k' or board[iSrc][jSrc] != 'K':
        return False
    
    downStep = 1
    upStep = -1
    rightStep = 1
    leftStep = -1
    
    # downCheck 
    for i in range(iSrc+1,8,downStep):
        if board[i][jSrc] in opponentPieces:
            threatLocation = indexToLocation(i,jSrc)
            threatBool = checkThreat(board,src,threatLocation,opponentPieces)
            if threatBool:
                print("check")
    
    #upCheck
    for i in range(iSrc-1,-1,upStep):
        if board[i][jSrc] in opponentPieces:
            threatLocation = indexToLocation(i,jSrc)
            threatBool = checkThreat(board,src,threatLocation,opponentPieces)
            if threatBool:
                print("check")

    # rightCheck                
    for j in range(jSrc+1,8,rightStep):
        if board[iSrc][j] in opponentPieces:
            threatLocation = indexToLocation(iSrc,j)
            threatBool = checkThreat(board,src,threatLocation,opponentPieces)
            if threatBool:
                print("check")
    
    for j in range(jSrc-1,-1,leftStep):
        if board[iSrc][j] in opponentPieces:
            threatLocation = indexToLocation(iSrc,j)
            threatBool = checkThreat(board,src,threatLocation,opponentPieces)
            if threatBool:
                print("check")
            
   
def checkThreat(board,kingLocation,threatLocation,opponentPieces):
    # iKing,jKing = convertLocation(kingLocation)
    iThreat,jThreat = convertLocation(threatLocation)
    threat = board[iThreat][jThreat]

    if threat not in opponentPieces:
        return False
    
    if threat == 'p':
        valid = validMovePawn(threatLocation,kingLocation)
    elif threat == 'P':
        valid = opponentValidMovePawn(threatLocation,kingLocation)
    elif threat == 'r' or threat == 'R':
        valid = validMoveRook(threatLocation,kingLocation)
    elif threat == 'n' or threat == 'N':
        valid = validMoveKnight(threatLocation,kingLocation)
    elif threat == 'b' or threat == 'B':
        valid = validMoveBishop(threatLocation,kingLocation)
    elif threat == 'q' or threat == 'Q':
        valid = validMoveQueen(threatLocation,kingLocation)
    elif threat == 'k' or threat == 'K':
        valid = validMoveKing(threatLocation,kingLocation)
    elif threat == '.':
        valid = False
            
    return valid
    
    

def opponentOrOwnPiece(board,src,dest,ownPieces):
    iDest, jDest = convertLocation(dest)
    pieceOnDest = board[iDest][jDest]
    
    if pieceOnDest in ownPieces:
        return False
    else:
        return True 

def validMovePawn(board,src,dest):
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
        return True
    elif diagnol2 in opponentPieces and iDest == iSrc - 1 and jDest == jSrc + 1:
        return True
    else:
        return False
    
    # Pawn promotion to be implemented, when reached at the end of opposite side
    
def opponentValidMovePawn(board,src,dest):
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
        return True
    elif diagnol2 in opponentPieces and iDest == iSrc + 1 and jDest == jSrc + 1:
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

def validMoveQueen(board,src,dest):
    if validMoveBishop(board,src,dest):
        return True
    elif validMoveRook(board,src,dest):
        return True
    else:
        return False

def validMoveKing(board,src,dest):
    global playerKingMoved, playerRook1Moved, playerRook2Moved, playerCastlingDone
    global oppeonentCastlingDone, oppeonentKingMoved, oppeonentRook1Moved, oppeonentRook2Moved
    
    iSrc,jSrc = convertLocation(src)
    iDest,jDest = convertLocation(dest)
    
    if playerCastlingDone == False:
        if (src == 'e1' and dest == 'h1') or (src == 'h1' and dest == 'e1'):
            if playerKingMoved == False and playerRook2Moved == False:
                if board[7][5] == '.' and board[7][6] == '.':
                    board[7][5] = 'r'
                    board[7][6] = 'k'
                    board[iSrc][jSrc] = '.'
                    board[iDest][jDest] = '.'
                    playerKingMoved = True
                    playerRook2Moved = True
                    playerCastlingDone = True
                    return "castlingMove"
        if (src == 'e1' and dest == 'a1') or (src == 'a1' and dest == 'e1') :
            if playerKingMoved == False and playerRook1Moved == False:
                if board[7][3] == '.' and board[7][2] == '.' and board[7][1] == '.':
                    board[7][3] = 'r'
                    board[7][2] = 'k'
                    board[iSrc][jSrc] = '.'
                    board[iDest][jDest] = '.'
                    playerKingMoved = True
                    playerRook1Moved = True
                    playerCastlingDone = True
                    return "castlingMove"
    
    if oppeonentCastlingDone == False:
        if (src == 'e8' and dest == 'h8') or (src == 'h8' and dest == 'e8'):
            if oppeonentKingMoved == False and oppeonentRook2Moved == False:
                if board[0][5] == '.' and board[0][6] == '.':
                    board[0][5] = 'r'
                    board[0][6] = 'k'
                    board[iSrc][jSrc] = '.'
                    board[iDest][jDest] = '.'
                    oppeonentKingMoved = True
                    oppeonentRook2Moved = True
                    oppeonentCastlingDone = True
                    return "castlingMove"
        if (src == 'e8' and dest == 'a8') or (src == 'a8' and dest == 'e8'):
            if oppeonentKingMoved == False and oppeonentRook1Moved == False:
                if board[0][3] == '.' and board[0][2] == '.' and board[0][1] == '.':
                    board[0][3] = 'r'
                    board[0][2] = 'k'
                    board[iSrc][jSrc] = '.'
                    board[iDest][jDest] = '.'
                    oppeonentKingMoved = True
                    oppeonentRook1Moved = True
                    oppeonentCastlingDone = True
                    return "castlingMove"
    
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
        print("Player 1 Turn")
        src,dest = moveUserInput(board, player=1)
        playerMove(board,src,dest)
        display_board(board)        
        
        print("Player 2 Turn")
        src,dest = moveUserInput(board, player=2)
        opponentMove(board,src,dest)
        display_board(board)


main()

# print(indexToLocation(0,0))
