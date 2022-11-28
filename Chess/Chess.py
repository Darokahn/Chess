"""TO DO:
!!!"Check" function
!!!add Castling
-"Checkmate" function
!!!abort for piece selection
-Pawn promotion

"""
pieceDict = {11 : "wr1", 12 : "wp", 13 : "no", 14: "no", 15 : "no", 16 : "no", 17 : "bp", 18 : "br1",
            21 : "wn", 22 : "wp", 23 : "no", 24 : "no", 25 : "no", 26 : "no", 27 : "bp", 28 : "bn",
            31 : "wb", 32 : "wp", 33 : "no", 34 : "no", 35 : "no", 36 : "no", 37 : "bp", 38 : "bb",
            41 : "wq", 42 : "wp", 43 : "no", 44 : "no", 45 : "no", 46 : "no", 47 : "bp", 48 : "bq",
            51 : "wk1", 52 : "wp", 53 : "no", 54 : "no", 55 : "no", 56 : "no", 57 : "bp", 58 : "bk1",
            61 : "wb", 62 : "wp", 63 : "no", 64 : "no", 65 : "no", 66 : "no", 67 : "bp", 68 : "bb",
            71 : "wn", 72 : "wp", 73 : "no", 74 : "no", 75 : "no", 76 : "no", 77 : "bp", 78 : "bn",
            81 : "wr1", 82 : "wp", 83 : "no", 84 : "no", 85 : "no", 86 : "no", 87 : "bp", 88 : "br1",
            99: "1"}

def saveFile(file):
    f = open(file, "w")
    f.write(str(pieceDict))
    f.close()
    
def openFile(file):
    f = open(file, "r")
    ditc = f.read()
    ditc = ditc.replace(": ", "").replace("{", "").replace("}", "").split(",")
    for i in range(len(ditc)):
        ditc[i] = ditc[i][3:].replace("\'", "")
    f.close
    x = 0
    for i in pieceDict:
        pieceDict[i] = ditc[x]
        x += 1

def imgPlace(key, Xcoor, Ycoor):
    #returns a list of pixels
    proxy = pieceDict[key][1]
    lits = []
    pieceImg = {"p" : [47, 57, 46, 56, 35, 45, 55, 65, 44, 54, 43, 53, 32, 42, 52, 62, 21, 31, 41, 51, 61, 71],
                "d" : [47, 57, 46, 56, 35, 45, 55, 65, 44, 54, 43, 53, 32, 42, 52, 62, 21, 31, 41, 51, 61, 71],
                "o" : [],
                "r" : [21, 31, 41, 51, 61, 71, 22, 32, 42, 52, 62, 72, 33, 43, 53, 63, 34, 44, 54, 64, 35, 45, 55, 65, 26, 36, 46, 56, 66, 76, 27, 47, 57, 77],
                "b" : [47, 57, 46, 36, 35, 45, 55, 65, 44, 54, 43, 53, 32, 42, 52, 62, 21, 31, 41, 51, 61, 71],
                "n" : [47, 57, 36, 46, 56, 66, 25, 35, 45, 55, 65, 24, 34, 44, 54, 64, 43, 53, 63, 32, 42, 52, 62, 21, 31, 41, 51, 61, 71],
                "q" : [47, 57, 26, 46, 56, 76, 25, 35, 45, 55, 65, 75, 34, 44, 54, 64, 43, 53, 32, 42, 52, 62, 21, 31, 41, 51, 61, 71],
                "k" : [21, 31, 41, 51, 61, 71, 32, 42, 52, 62, 23, 33, 43, 53, 63, 73, 24, 34, 44, 54, 64, 74, 45, 55, 36, 46, 56, 66, 47, 57]}
    for i in pieceImg[proxy]:
        lits.append(str(int(str(i)[0])+Xcoor-1) + "/" + str(int(str(i)[1])+Ycoor))
    return lits

def printBoard():
    board = "\n\n\n"
    tilecolor = 1
    for i in range(1,64):
        y = abs(64-i)
        tilecolor = tilecolor * -1
        if (y % 8 == 0):
            tilecolor = tilecolor * -1
        for i in range(1,64):
            x = i
            position = [((x+8) // 8), ((y+8) // 8)]
            positionSimple = str(position[0])+str(position[1])
            Ycoor = (position[1]*8)-8
            Xcoor = (position[0]*8)-8
            if (x % 8 == 0):
                tilecolor = tilecolor * -1
            if str(x) + "/" + str(y) in imgPlace(int(positionSimple), Xcoor, Ycoor):
                if pieceDict[int(positionSimple)][0] == "w":
                    board = board + "██"
                else:
                    board = board + "||"
            else:
                board = board + str(tilecolor).replace("-1", "00").replace("1", "  ")
        board = board + "\n"
    print(board)

def raycast(tile, newTile, moveDirX = None, moveDirY = None):
    if (tile != None) and (newTile != None):
        if int(str(tile)[0]) == int(str(newTile)[0]):
            moveDirX = 0
        elif int(str(tile)[0]) > int(str(newTile)[0]):
            moveDirX = -1
        elif int(str(tile)[0]) < int(str(newTile)[0]):
            moveDirX = 1

        if int(str(tile)[1]) == int(str(newTile)[1]):
            moveDirY = 0
        elif int(str(tile)[1]) > int(str(newTile)[1]):
            moveDirY = -1
        elif int(str(tile)[1]) < int(str(newTile)[1]):
            moveDirY = 1
    foundTile = [0, "no"]
    x = int(str(tile)[0])+moveDirX
    y = int(str(tile)[1])+moveDirY
    newDict = amendHypothetical(tile, newTile)
    while foundTile == [0, "no"]:
        try:
            foundTile[1] = pieceDict[int(str(x)+str(y))]
        except:
            break
        if int(str(x)+str(y)) == newTile:
            foundTile[0] = 1
        x = x + moveDirX
        y = y + moveDirY
    return foundTile 
    
def pawnUnmoved(tile, newTile, color):
    tile = str(tile)
    newTile = str(newTile)
    moveDir = int(color.replace("b", "-1").replace("w","1"))
    if newTile == tile[0]+str(int(tile[1])+moveDir):
        return True
    elif newTile == tile[0]+str(int(tile[1])+2*moveDir):
        if pieceDict[int(tile[0]+str(int(tile[1])+moveDir))] == "no":
            return True
        else:
            pass
    elif newTile == str(int(tile[0])+1)+str(int(tile[1])+moveDir):
        if pieceDict[int(newTile)][0] == color.replace("b","x").replace("w", "y").replace("x", "w").replace("y", "b"):
            return True
    elif newTile == str(int(tile[0])-1)+str(int(tile[1])+moveDir):
        if pieceDict[int(newTile)][0] == color.replace("b","x").replace("w", "y").replace("x", "w").replace("y", "b"):
            return True
    else:
        pass

def pawnMoved(tile, newTile, color):
    tile = str(tile)
    newTile = str(newTile)
    moveDir = int(color.replace("w", "1").replace("b","-1"))
    if newTile == tile[0]+str(int(tile[1])+moveDir):
        return True
    elif newTile == str(int(tile[0])+1)+str(int(tile[1])+moveDir):
        if pieceDict[int(newTile)][0] == color.replace("b","x").replace("w", "y").replace("x", "w").replace("y", "b"):
            return True
    elif newTile == str(int(tile[0])-1)+str(int(tile[1])+moveDir):
        if pieceDict[int(newTile)][0] == color.replace("b","x").replace("w", "y").replace("x", "w").replace("y", "b"):
            return True
    else:
        pass

def rook(tile, newTile):
    if (str(tile)[0] == str(newTile)[0]) or (str(tile)[1] == str(newTile)[1]):
        if raycast(tile, newTile)[0] == 1:
            return True

def castle(color, direction, pieceDict):
    if color == "b":
        if direction == "king":
            if pieceDict[58] == "bk1":
                if pieceDict[88] == "br1":
                    if raycast(58, 88)[0] == 1:
                        pieceDict = amend(58, 78)
                        return amend(88, 68)
                    else:
                        print("You cannot castle kingside since there are pieces in the way.")
                        return move(color)
                else:
                    print("You cannot castle kingside since your rook has moved.")
                    return move(color)
            else:
                print("You cannot castle since your king has moved.")
                return move(color)
                        
        elif direction == "queen":
            if pieceDict[58] == "bk1":
                if pieceDict[18] == "br1":
                    if raycast(58, 18)[0] == 1:
                        pieceDict = amend(58, 28)
                        return amend(18, 38)
                    else:
                        print("You cannot castle queenside since there are pieces in the way.")
                        return move(color)
                else:
                    print("You cannot castle queenside since your rook has moved.")
                    return move(color)
            else:
                print("You cannot castle since your king has moved.")
                return move(color)
    else:
        if direction == "king":
            if pieceDict[51] == "wk1":
                if pieceDict[81] == "wr1":
                    if raycast(51, 81)[0] == 1:
                        pieceDict = amend(51, 71)
                        return amend(81, 61)
                    else:
                        print("You cannot castle kingside since there are pieces in the way.")
                        return move(color)
                else:
                    print("You cannot castle kingside since your rook has moved.")
                    return move(color)
            else:
                print("You cannot castle since your king has moved.")
                return move(color)
        elif direction == "queen":
            if pieceDict[51] == "wk1":
                if pieceDict[11] == "wr1":
                    if raycast(51, 11)[0] == 1:
                        pieceDict = amend(51, 21)
                        return amend(11, 31)
                    else:
                        print("You cannot castle queenside since there are pieces in the way.")
                        return move(color)
                else:
                    print("You cannot castle queenside since your rook has moved.")
                    return move(color)
            else:
                print("You cannot castle since your king has moved.")
                return move(color)

def knight(tile, newTile):
    value = False
    for i in range(-2, 3):
        x = i
        for i in range (-2, 3):
            y = i
            if (abs(x)+abs(y) == 3) and (x*y != 0):
                try:
                    if int(str(int(str(tile)[0])+x)+str(int(str(tile)[1])+y)) == newTile:
                        value = True
                    else:
                        continue
                except:
                    continue
            else:
                continue
    if not value:
        x = x
    else:
        return value

def bishop(tile, newTile):
    if abs(int(str(tile)[0])-int(str(newTile)[0])) / abs(int(str(tile)[1])-int(str(newTile)[1])) == 1:
        if raycast(tile, newTile)[0] == 1:
            return True

def queen(tile, newTile):
    if rook(tile, newTile) or bishop(tile, newTile):
        return True

def king(tile, newTile):
    for i in range(-1, 2):
        x = i
        for i in range(-1, 2):
            y = i
            if abs(x)+abs(y) != 0:
                if int(str(int(str(tile)[0])+x)+str(int(str(tile)[1])+y)) == newTile:
                    return True

def check(color, pieceDict):
    enemyColor = color.replace("w", "x").replace("b", "y").replace("x", "b").replace("y", "w")
    moveDir = int(color.replace("b", "-1").replace("w", "1"))
    for i in pieceDict:
        if color+"k" in pieceDict[i]:
            kingPos = i
            break
    x = str(kingPos)[0]
    y = str(kingPos)[1]
    checking = []
    # I was going to use a bunch of for loops here, but they were giving me too much trouble and I decided to brute force it instead.
    if raycast(kingPos, None, 1, 0)[1] in [enemyColor+"r", enemyColor+"q"]:
        checking.append(raycast(kingPos, None, 1, 0)[1])
    if raycast(kingPos, None, 0, 1)[1] in [enemyColor+"r", enemyColor+"q"]:
        checking.append(raycast(kingPos, None, 0, 1)[1])
    if raycast(kingPos, None, -1, 0)[1] in [ enemyColor+"r", enemyColor+"q"]:
        checking.append(raycast(kingPos, None, -1, 0)[1])
    if raycast(kingPos, None, 0, -1)[1] in [enemyColor+"r", enemyColor+"q"]:
        checking.append(raycast(kingPos, None, 0, -1)[1])
    if raycast(kingPos, None, 1, 1)[1] in [enemyColor+"b", enemyColor+"q"]:
        checking.append(raycast(kingPos, None, 1, 1)[1])
    if raycast(kingPos, None, 1, -1)[1] in [enemyColor+"b", enemyColor+"q"]:
        checking.append(raycast(kingPos, None, 1, -1)[1])
    if raycast(kingPos, None, -1, 1)[1] in [enemyColor+"b", enemyColor+"q"]:
        checking.append(raycast(kingPos, None, -1, 1)[1])
    if raycast(kingPos, None, -1, -1)[1] in [enemyColor+"b", enemyColor+"q"]:
        checking.append(raycast(kingPos, None, -1, -1)[1])
    for i in [-2, -1, 1, 2]:
        addX = i
        for i in [-2, -1, 1, 2]:
            addY = i
            if abs(addX) + abs(addY) == 3:
                if not ((str(int(x)+addX) in ["0", "-1", "-2", "9", "10", "11"]) or (str(int(y)+addY) in ["0", "-1", "-2", "9", "10", "11"])):
                    if pieceDict[int(str(int(x)+addX)+str(int(y)+addY))] == enemyColor+"n":
                        checking.append(pieceDict[int(str(int(x)+addX)+str(int(y)+addY))])
                    else:
                        continue
            else:
                continue
    if not ((str(int(x)+1) in ["0", "9"]) or (str(int(y)+moveDir) in ["0", "9"])):
        if pieceDict[int(str(int(x)+1)+str(int(y)+moveDir))] in [enemyColor+"p", enemyColor+"d"]:
            checking.append(pieceDict[int(str(int(x)+1)+str(int(y)+moveDir))])
    if not ((str(int(x)-1) in ["0", "9"]) or (str(int(y)+moveDir) in ["0", "9"])):
        if pieceDict[int(str(int(x)-1)+str(int(y)+moveDir))] in [enemyColor+"p", enemyColor+"d"]:
            checking.append(pieceDict[int(str(int(x)-1)+str(int(y)+moveDir))])
    return checking
        

def move(color):
    valid = 0
    while valid != 1:
        tile = int(input("Which piece would you like to move, " + color.replace("w", "white").replace("b", "black") + "? "))
        try:
            pieceDict[int(tile)] 
        except:
            print("That is not a valid piece to choose.")
            continue
        if pieceDict[int(tile)][0] == color:
            valid = 1
        else:
            print("That is not your piece.")
            continue
    valid = 0
    while valid != 1:
        newTile = input("Where should this piece move? ")
        if newTile[:6] == "castle":
            return castle(color, newTile[7:], pieceDict)
        if newTile == "abort":
            return move(color)
        newTile = int(newTile)
        try:
            pieceDict[newTile]
        except:
            print("That is not a vaild square on the board.")
        if pieceDict[newTile][0] != color:
            if check(color, amendHypothetical(tile, newTile)) == []:
                if pieceDict[tile][1] == "p":
                    if pawnUnmoved(tile, newTile, color):
                        valid = 1
                    else:
                        print("That piece cannot move like that.")
                        continue
                    #firstmove pawn conditions
                elif pieceDict[tile][1] == "r":
                    if rook(tile, newTile):
                        valid = 1
                    else:
                        print("That piece cannot move like that.")
                        continue
                    #rook conditions
                elif pieceDict[tile][1] == "n":
                    if knight(tile, newTile):
                        valid = 1
                    else:
                        print("That piece cannot move like that.")
                        continue
                    #knight conditions
                elif pieceDict[tile][1] == "b":
                    if bishop(tile, newTile):
                        valid = 1
                    else:
                        print("That piece cannot move like that.")
                        continue
                    #bishop conditions
                elif pieceDict[tile][1] == "q":
                    if rook(tile, newTile) or bishop(tile, newTile):
                        valid = 1
                    else:
                        print("That piece cannot move like that.")
                        continue
                    #queen condtions
                elif pieceDict[tile][1] == "k":
                    if king(tile, newTile):
                        valid = 1
                    else:
                        print("That piece cannot move like that.")
                        continue
                    #king conditions
                elif pieceDict[tile][1] == "d":
                    if pawnMoved(tile, newTile, color):
                        valid = 1
                    else:
                        print("That piece cannot move like that.")
                        continue
                    #moved pawn conditions
                return amend(tile, newTile)
            else:
                print("That move puts your king into danger!")
                continue
        else:
            print("That piece is your color.")
            continue

def amend(tile, newTile):
    pieceDict[tile] = pieceDict[tile].replace("p", "d").replace("1", "")
    pieceDict[newTile] = pieceDict[tile]
    pieceDict[tile] = "no"
    return pieceDict

def amendHypothetical(tile, newTile):
    newDict = pieceDict.copy()
    newDict[tile] = newDict[tile].replace("p", "d").replace("1", "")
    newDict[newTile] = newDict[tile]
    newDict[tile] = "no"
    return newDict

def play():
    game = input("write a file name here. This will be your game's save file. If the file you type already exists, that file will be loaded. ")
    try:
        openFile(game)
        overwrite = input("it looks like this game exists already. Would you like to overwrite it? Type \"1\" to open it and then overwrite, \"2\" to open it and leave it alone, and \"3\" to start a fresh game with this filename.")
    except:
        saveFile(game)
        overwrite = "1"
    if overwrite == "3":
        global pieceDict
        pieceDict = {11: 'wr1', 12: 'wp', 13: 'no', 14: 'no', 15: 'no', 16: 'no', 17: 'bp', 18: 'br1', 21: 'wn', 22: 'wp', 23: 'no', 24: 'no', 25: 'no', 26: 'no', 27: 'bp', 28: 'bn', 31: 'wb', 32: 'wp', 33: 'no', 34: 'no', 35: 'no', 36: 'no', 37: 'bp', 38: 'bb', 41: 'wq', 42: 'wp', 43: 'no', 44: 'no', 45: 'no', 46: 'no', 47: 'bp', 48: 'bq', 51: 'wk1', 52: 'wp', 53: 'no', 54: 'no', 55: 'no', 56: 'no', 57: 'bp', 58: 'bk1', 61: 'wb', 62: 'wp', 63: 'no', 64: 'no', 65: 'no', 66: 'no', 67: 'bp', 68: 'bb', 71: 'wn', 72: 'wp', 73: 'no', 74: 'no', 75: 'no', 76: 'no', 77: 'bp', 78: 'bn', 81: 'wr1', 82: 'wp', 83: 'no', 84: 'no', 85: 'no', 86: 'no', 87: 'bp', 88: 'br1', 99: '1'}
    printBoard()
    print("""welcome to chess. If you have not already, please run this code in the terminal of your device. click "run" > "run current script in terminal". You should then resize the terminal to see the chessboard, as you will be zoomed in and somewhat distorted by default. Holding ctrl and scrolling will zoom the terminal window. Note that visual errors will occur if your terminal is in "fullscreen" mode. Press Enter when you are ready to begin.""")
    input("")
    print("""When it is your turn, select a piece by writing the "x" coordinate followed by the "y" coordinate. For example, to select the piece on the third column and the second row, You would type "32". Then, type the destination for that piece in the same manner. If the move you have selected is valid, the piece will update automatically.
additional commands:
- 'castle (queen/king)' will perform a move called "castling" where, if neither piece has moved from its starting position, the king and rook will meet in the middle and swap positions. writing "queen" will castle toward the queen's side of the board, and "king" will castle kingside.
- 'abort' will interrupt your current move and allow you to select a different piece.""")
    checkmate = 0
    while checkmate == 0:
        player = int(pieceDict[99])
        move(str(player).replace("-1", "b").replace("1", "w"))
        printBoard()
        if check(str(player).replace("-1", "w").replace("1", "b"), pieceDict):
            print("Check on " +str(player).replace("-1", "white").replace("1", "black")+ "!")
        pieceDict[99] = int(pieceDict[99])*-1
        if overwrite in ["1", "3"]:
            saveFile(game)
play()