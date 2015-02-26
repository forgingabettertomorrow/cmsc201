# File:    project1.py
# Author:  victor gee
# Date:    11/22/2014
# Section: 7
# E-mail:  vicgee1@umbc.edu
# Description:
# This file contains python code that will allow
# two players to play against each other in games
# of Connect Four.

def boardSize():
    # asks user for 2 values to create a playing board
    # Input: no arguments taken
    # Output: the assembled board back to the main

    myBoard1, underscores = [], ""
    # if user enters rows or columns less than four, ask for a valid entry
    # or if the user enters something with ascii values outside 0 and 9
    inputCheck = False
    while inputCheck == False:
        rows = input("Please enter a number of rows: ")
        while rows.isdigit() == False or int(rows) < 5:
            inputCheck = False
            rows = input("Please enter a valid number.")
        if int(rows) >= 5:
            inputCheck = True

    inputCheck1 = False
    while inputCheck1 == False:
        columns = input("Please enter a number of columns: ")
        while columns.isdigit() == False or int(columns) < 5:
            columns = input("Please enter a valid number.")
            inputCheck1 = False
        if int(columns) >= 5:
            inputCheck1 = True

    myBoard1 = [['_' for x in range(int(columns))] for y in range(int(rows))]
    # return the board that was created to the main
    return myBoard1

# alternates between players
def player(token1):
    # Input: token indicating whose turn it is
    # Outputs: prints on screen whose turn it is and returns token to call
    if token1 == 1:
        token1 = 2
        print("Player 2's turn.")
    elif token1 == 2:
        token1 = 1
        print("Player 1's turn.")
    return token1

def move(myBoard2, token2):
    # user enters a column they would like to insert a disc
    # Input: the playing board and the player making the move
    # Output: the column and row positino of last play, the revised board, and whether the move was successfully made

    # checks that the column entered is valid
    columns = len(myBoard2[0])
    playable = False
    moveSuccess, inputCheck, fullColumn = False, False, False

    # while the tile is occupied, it's not playable and must search again
    while playable != True:

        while inputCheck == False:
            lastMove1 = input("Please enter a move: ")
            while lastMove1.isdigit() == False or int(lastMove1) < 0 or int(lastMove1) > columns:
                inputCheck = False
                lastMove1 = input("Please enter a valid move.")
            if int(lastMove1) > 0 and int(lastMove1) <= columns:
                inputCheck = True

        ## if the input is validated check if the column is occupied
        ## subtract one because the user input is one ahead a position in an array
        lastMove1 = int(lastMove1) -1
        for i in range(0, len(myBoard2), 1):
            if myBoard2[i][lastMove1] == '_':
                playable = True
                moveSuccess = True
                lastRow = i
            else:
                inputCheck = False


    # if the space is available, put an X or O depending on token value
    if playable:
        if token2 == 1:
            myBoard2[lastRow][lastMove1] = 'X'
        else:
            myBoard2[lastRow][lastMove1] = 'O'
    else:
        lastRow = 0

    # returns the last column played and the myBoard2 reflecting the players move
    return lastMove1, myBoard2, moveSuccess, lastRow

def printBoard(myBoard3):
    # prints to the screen the board with reflected changes
    # Input: the playing board
    line = ''
    # DO NOT DELETE ME!!!
    for i in range(len(myBoard3)):
        for e in myBoard3[i]:
            line += e
        print(line, end = '\n')
        line = ''

def checkWin(myBoard4, lastColPlayed1, lastRowPlayed1):
    # checks for a winner based on the last move made
    # Inputs: playing board, last column and row played

    tally1, tally2 = 0, 0
    # check horizontally if player 1 wins
    for i in range(len(myBoard4[0])):
        if myBoard4[lastRowPlayed1][i] == 'X':
            tally1 += 1
        else:
            tally1 = 0
        if tally1 == 4:
            return True
#        elif tally1 < 4:
#            return False

    # check horizontally if player 2 wins
    for i in range(len(myBoard4[0])):
        if myBoard4[lastRowPlayed1][i] == 'O':
            tally1 += 1
        else:
            tally1 = 0
        if tally1 == 4:
            return True
#        elif tally1 < 4:
#            return False

    # check vertically if player 1 wins
    for i in range(len(myBoard4)):
        if myBoard4[i][lastColPlayed1] == 'X':
            tally1 += 1
        else:
            tally1 = 0
        if tally1 == 4:
            return True
#    elif tally1 < 4:
#        return False

    # check vertically if player 2 wins
    for i in range(len(myBoard4)):
        if myBoard4[i][lastColPlayed1] == 'O':
            tally2 += 1
        else:
            tally2 = 0
        if tally2 == 4:
            return True
#    elif tally2 < 4:
#        return False

    # check along diagonals for a winner
    for x in range(0, len(myBoard4[0])-3, 1):
        for y in range(3, len(myBoard4[0])):
            #print(myBoard4[x][y], ' ', myBoard4[x+1][y-1], ' ', myBoard4[x+2][y-2], ' ', myBoard4[x+3][y-3])
            if (myBoard4[x][y] == 'X') and (myBoard4[x+1][y-1] == 'X') and (myBoard4[x+2][y-2] == 'X') and (myBoard4[x+3][y-3] == 'X'):
                #print("Player 1 won!!!")
                return True

    for x in range(len(myBoard4[0])-3):
        for y in range(len(myBoard4[0]) - 3):
            #print(myBoard4[x][y], ' ', myBoard4[x+1][y+1], ' ', myBoard4[x+2][y+2], ' ', myBoard4[x+3][y+3])
            if (myBoard4[x][y] == 'X') and (myBoard4[x+1][y+1] == 'X') and (myBoard4[x+2][y+2] == 'X') and (myBoard4[x+3][y+3] == 'X'):
                #print("Player 1 won!!!")
                return True

    # check along diagonals to see if p2 won
    for x in range(0, len(myBoard4[0])-3, 1):
        for y in range(3, len(myBoard4[0])):
            #print(myBoard4[x][y], ' ', myBoard4[x+1][y-1], ' ', myBoard4[x+2][y-2], ' ', myBoard4[x+3][y-3])
            if (myBoard4[x][y] == 'O') and (myBoard4[x+1][y-1] == 'O') and (myBoard4[x+2][y-2] == 'O') and (myBoard4[x+3][y-3] == 'O'):
                #print("Player 2 won!!!")
                return True

    tally3 = 0
    for x in range(len(myBoard4[0])-3):
        for y in range(len(myBoard4[0]) - 3):
            #print(myBoard4[x][y], ' ', myBoard4[x+1][y+1], ' ', myBoard4[x+2][y+2], ' ', myBoard4[x+3][y+3])
            if (myBoard4[x][y] == 'O') and (myBoard4[x+1][y+1] == 'O') and (myBoard4[x+2][y+2] == 'O') and (myBoard4[x+3][y+3] == 'O'):
                #print("Player 2 won!!!")
                return True

    if tally3 == 0:
        return False


def drawChecker(myBoard5):
    # checks for any underscores which would indicate a guess has not been made
    # Inputs: playing board
    notOver = 0
    for i in range(len(myBoard5)):
        for j in range(len(myBoard5[0])):
            if myBoard5[i][j] == '_':
                notOver = 1
    if notOver == 0:
        print("The game is a draw!")
        return True
    else:
        return False

##    for i in range(len(myBoard5[0])):
##        for j in myBoard5[i]:
##            for k in myBoard5[]
##            if j == '_':
##                return False
##    return True

def replayCheck():
    replay = str(input("Would you like to play again (y/n)?")).upper()
    while replay != str('N') and replay != str('Y'):
        replay = str(input("Please, only enter (y/n): ")).upper()
    if replay == 'N':
        exit()
    elif replay == 'Y':
        return True

def main():
    print("Welcome to Connect Four.")
    replay, underScoreCheck = True, False
    # while the player wants to keep playing, loop these
    moveSuccess = True
    while replay == True:
        token, lastColPlayed, checkWinResult, drawCheck = 2, 0, False, False
        myBoard = boardSize()
        # while the game is not over (ie. no winner and the game is not a draw), continue looping
        print(checkWinResult, drawCheck)
        while checkWinResult == False and drawCheck == False:
            if moveSuccess:
                token = player(token)
            printBoard(myBoard)
            lastColPlayed, myBoard, moveSuccess, lastRowPlayed = move(myBoard, token)
            checkWinResult = checkWin(myBoard, lastColPlayed, lastRowPlayed)
            drawCheck = drawChecker(myBoard)
            if checkWinResult == True:
                print("Player", token, "wins!!")
                printBoard(myBoard)
        replay = replayCheck()
main()
