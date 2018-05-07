# Nadia Calvina Liandi Putri
# Student ID: 22059517
# Unit: CITS4406 Problem Solving and Programming
# Assessment: Project 2

from random import randrange
from graphics import *
from time import sleep

# Controls the main flow of the program
def main():
    #--------------------- CREATES NEW GAME -------------------------
    win = GraphWin("5-by-5 2048",640,490)
    win.setBackground(color_rgb(241, 241, 241))
    quitButton, score, scoreVal, status, newGameButton, humanButton, computerButton, human, computer = makeInterface(win)
    boxUp01, boxUp02, boxUp03, boxLeft01, boxLeft02, boxLeft03, boxRight01, boxRight02, boxRight03, boxDown01, boxDown02, boxDown03 = makeBoardInterface(win)
    continueGame = True
    firstRound = True
    restart = False
    newRow = -1
    newCol = -1

    # Change this to control time delay when computer player is chosen
    pause = 1
    
    #--------------------- PLAYS GAME -------------------------
    # While continueGame is True, the game window will remain open and functional.
    while continueGame == True:
        # If the game is played for the first time (firstRound) or game stopped because of game over (restart), the program will wait for a mouse click.
        if firstRound == True or restart == True:
            getClick = win.getMouse()
        humanPlayer = False
        computerPlayer = False
        playerChosen = False
        # If new game button is clicked, the human or computer player option will be shown.
        # The status will prompt the user to choose a player.
        if clicked(getClick, newGameButton) == True:
            humanButton.setFill(color_rgb(180, 217, 231))
            humanButton.setOutline(color_rgb(180, 217, 231))
            human.setTextColor(color_rgb(72, 72, 72))
            computerButton.setFill(color_rgb(180, 217, 231))
            computerButton.setOutline(color_rgb(180, 217, 231))
            computer.setTextColor(color_rgb(72, 72, 72))
            status.setText("choose a player")
            score.setText("0")
            scoreVal = 0
            if restart == True:
                eraseBoardInterface(boardVal)

            # While the user has not chosen a player, the game will keep waiting for a mouse click.
            # Once a player is chosen, the game will show the chosen player as "active" and the game board will be filled in.
            while playerChosen == False:
                getClick = win.getMouse()
                if clicked(getClick, humanButton) == True:
                    humanPlayer = True
                    status.setText("you will be playing")
                    computerButton.setFill(color_rgb(220, 221, 221))
                    computerButton.setOutline(color_rgb(220, 221, 221))
                    computer.setTextColor(color_rgb(172, 172, 172))
                    gameBoard, gameColumns = createBoard()
                    fillDefault(gameBoard, gameColumns)
                    checkBoard = gameBoard[:]
                    boardVal = drawBoardInterface(win, checkBoard, gameBoard, newRow, newCol)
                    playerChosen = True
                elif clicked(getClick, computerButton) == True:
                    computerPlayer = True
                    status.setText("a computer will be playing")
                    humanButton.setFill(color_rgb(220, 221, 221))
                    humanButton.setOutline(color_rgb(220, 221, 221))
                    human.setTextColor(color_rgb(172, 172, 172))
                    gameBoard, gameColumns = createBoard()
                    fillDefault(gameBoard, gameColumns)
                    checkBoard = gameBoard[:]
                    boardVal = drawBoardInterface(win, checkBoard, gameBoard, newRow, newCol)
                    playerChosen = True
                elif clicked(getClick, quitButton) == True:
                    continueGame = False
                    playerChosen = True
                    win.close()

        # Otherwise, if user clicks quit, the window will close.
        elif clicked(getClick, quitButton) == True:
            continueGame = False
            win.close()

        #--------------------- HUMAN PLAYER -------------------------
        while humanPlayer == True:
            # A copy of the game board and its columns are created, to be checked later on for legal moves 
            checkBoard = gameBoard[:]

            # While legal move is still possible, the game will wait for user click, and returns the corresponding functions.
            if gameOver(gameBoard, gameColumns) == False:
                getClick = win.getMouse()
                if clicked(getClick, boxUp01) == True or clicked(getClick, boxUp02) == True or clicked(getClick, boxUp03) == True:
                    eraseBoardInterface(boardVal)
                    gameBoard, gameColumns = moveUp(slideUp, gameBoard, gameColumns)
                    gameBoard, gameColumns, newRow, newCol = addNew(moveUp, gameBoard, gameColumns)
                    boardVal = drawBoardInterface(win, checkBoard, gameBoard, newRow, newCol)
                    if isLegal(checkBoard, gameBoard) == True:
                        status.setText("moving up successful")
                        scoreVal = updateScore(scoreVal, score, 1)
                    else:
                        status.setText("movement not possible")
                        scoreVal = updateScore(scoreVal, score, -1)
                elif clicked(getClick, boxDown01) == True or clicked(getClick, boxDown02) == True or clicked(getClick, boxDown03) == True:
                    eraseBoardInterface(boardVal)
                    gameBoard, gameColumns = moveDown(moveUp, rotateClockwise, rotateAntiClockwise, gameBoard, gameColumns)
                    gameBoard, gameColumns, newRow, newCol = addNew(moveDown, gameBoard, gameColumns)
                    boardVal = drawBoardInterface(win, checkBoard, gameBoard, newRow, newCol)
                    if isLegal(checkBoard, gameBoard) == True:
                        status.setText("moving down successful")
                        scoreVal = updateScore(scoreVal, score, 1)
                    else:
                        status.setText("movement not possible")
                        scoreVal = updateScore(scoreVal, score, -1)
                elif clicked(getClick, boxLeft01) == True or clicked(getClick, boxLeft02) == True or clicked(getClick, boxLeft03) == True:
                    eraseBoardInterface(boardVal)
                    gameBoard, gameColumns = moveLeft(moveUp, rotateClockwise, rotateAntiClockwise, gameBoard, gameColumns)
                    gameBoard, gameColumns, newRow, newCol = addNew(moveLeft, gameBoard, gameColumns)
                    boardVal = drawBoardInterface(win, checkBoard, gameBoard, newRow, newCol)
                    if isLegal(checkBoard, gameBoard) == True:
                        status.setText("moving left successful")
                        scoreVal = updateScore(scoreVal, score, 1)
                    else:
                        status.setText("movement not possible")
                        scoreVal = updateScore(scoreVal, score, -1)
                elif clicked(getClick, boxRight01) == True or clicked(getClick, boxRight02) == True or clicked(getClick, boxRight03) == True:
                    eraseBoardInterface(boardVal)
                    gameBoard, gameColumns = moveRight(moveUp, rotateClockwise, rotateAntiClockwise, gameBoard, gameColumns)
                    gameBoard, gameColumns, newRow, newCol = addNew(moveRight, gameBoard, gameColumns)
                    boardVal = drawBoardInterface(win, checkBoard, gameBoard, newRow, newCol)
                    if isLegal(checkBoard, gameBoard) == True: 
                        status.setText("moving right successful")
                        scoreVal = updateScore(scoreVal, score, 1)
                    else:
                        status.setText("movement not possible")
                        scoreVal = updateScore(scoreVal, score, -1)
                elif clicked(getClick, quitButton) == True:
                    continueGame = False
                    win.close()
                elif clicked(getClick, newGameButton) == True:
                    restart = False
                    eraseBoardInterface(boardVal)
                    status.setText("click new game to start")
                    humanPlayer = False
                    firstRound = False

            # No legal moves possible
            elif gameOver(gameBoard, gameColumns) == True:
                restart = True
                statusOver = "game over with final score: " + str(scoreVal)
                status.setText(statusOver)
                humanPlayer = False
                firstRound = False
                        
        #--------------------- COMPUTER PLAYER -------------------------
        while computerPlayer == True:
            # Gameplay starts
                       
            # A copy of the game board and its columns are created, to be checked later on for legal moves 
            checkBoard = gameBoard[:]

            # While legal move is still possible and user does not click quit or new game, the computer will select a random move and keeps playing.
            move = "none"
            move = randomMove()
            getClick = win.checkMouse()
            sleep(pause)
            
            if gameOver(gameBoard, gameColumns) == False:
                if getClick == None:
                    if move == "up":
                        eraseBoardInterface(boardVal)
                        gameBoard, gameColumns = moveUp(slideUp, gameBoard, gameColumns)
                        gameBoard, gameColumns, newRow, newCol = addNew(moveUp, gameBoard, gameColumns)
                        boardVal = drawBoardInterface(win, checkBoard, gameBoard, newRow, newCol)
                        if isLegal(checkBoard, gameBoard) == True:
                            status.setText("moving up successful")
                            scoreVal = updateScore(scoreVal, score, 1)
                        else:
                            status.setText("movement not possible")
                            scoreVal = updateScore(scoreVal, score, -1)
                    elif move == "down":
                        eraseBoardInterface(boardVal)
                        gameBoard, gameColumns = moveDown(moveUp, rotateClockwise, rotateAntiClockwise, gameBoard, gameColumns)
                        gameBoard, gameColumns, newRow, newCol = addNew(moveDown, gameBoard, gameColumns)
                        boardVal = drawBoardInterface(win, checkBoard, gameBoard, newRow, newCol)
                        if isLegal(checkBoard, gameBoard) == True:
                            status.setText("moving down successful")
                            scoreVal = updateScore(scoreVal, score, 1)
                        else:
                            status.setText("movement not possible")
                            scoreVal = updateScore(scoreVal, score, -1)
                    elif move == "left":
                        eraseBoardInterface(boardVal)
                        gameBoard, gameColumns = moveLeft(moveUp, rotateClockwise, rotateAntiClockwise, gameBoard, gameColumns)
                        gameBoard, gameColumns, newRow, newCol = addNew(moveLeft, gameBoard, gameColumns)
                        boardVal = drawBoardInterface(win, checkBoard, gameBoard, newRow, newCol)
                        if isLegal(checkBoard, gameBoard) == True:
                            status.setText("moving left successful")
                            scoreVal = updateScore(scoreVal, score, 1)
                        else:
                            status.setText("movement not possible")
                            scoreVal = updateScore(scoreVal, score, -1)
                    elif move == "right":
                        eraseBoardInterface(boardVal)
                        gameBoard, gameColumns = moveRight(moveUp, rotateClockwise, rotateAntiClockwise, gameBoard, gameColumns)
                        gameBoard, gameColumns, newRow, newCol = addNew(moveRight, gameBoard, gameColumns)
                        boardVal = drawBoardInterface(win, checkBoard, gameBoard, newRow, newCol)
                        if isLegal(checkBoard, gameBoard) == True: 
                            status.setText("moving right successful")
                            scoreVal = updateScore(scoreVal, score, 1)
                else:
                    if clicked(getClick, quitButton) == True:
                        continueGame = False
                        computerPlayer = False
                        win.close()
                    elif clicked(getClick, newGameButton) == True:
                        restart = False
                        eraseBoardInterface(boardVal)
                        status.setText("click new game to start")
                        computerPlayer = False
                        firstRound = False

            # No legal moves possible
            elif gameOver(gameBoard, gameColumns) == True:
                restart = True
                statusOver = "game over with final score: " + str(scoreVal)
                status.setText(statusOver)
                computerPlayer = False
                firstRound = False

#---------------SECTION 1. GRAPHICS-------------------
# The following section will create the graphic environment of the program.

# makeInterface function will create the buttons, texts, status panel, and score board.
# Input parameter: graphics window (win)
# Output parameters:
# - Buttons (newGameButton, quitButton, humanButton, computerButton)
# - Text (score, scoreVal, status, human, computer)
# scoreVal stores the current value of the score, and score will display the value of scoreVal.
# human/humanButton and computer/computerButton will be used to modify the button to active/inactive state.
def makeInterface(win):
    #-------PANELS----------
    #Score board
    scoreTitle = Text(Point(87, 30), "SCORE:")
    scoreTitle.setStyle("bold")
    scoreTitle.setSize(12)
    scoreTitle.draw(win)
    scoreBoard = Rectangle(Point(58, 45), Point(200, 75))
    scoreBoard.setFill(color_rgb(209, 235, 235))
    scoreBoard.setOutline(color_rgb(209, 235, 235))
    scoreBoard.draw(win)
    scoreVal = 0
    score = Text(Point(129, 60), scoreVal)
    score.setStyle("bold")
    score.setSize(10)
    score.draw(win)
    #Status panel
    statusTitle = Text(Point(330, 30), "STATUS:")
    statusTitle.setStyle("bold")
    statusTitle.setSize(12)
    statusTitle.draw(win)
    statusPanel = Rectangle(Point(300, 45), Point(590, 75))
    statusPanel.setFill(color_rgb(209, 235, 235))
    statusPanel.setOutline(color_rgb(209, 235, 235))
    statusPanel.draw(win)
    status = Text(Point(450, 60), "click new game to start")
    status.setStyle("bold")
    status.setSize(10)
    status.draw(win)
    #-------BUTTONS----------
    #New game button
    newGameButton = Rectangle(Point(58, 140), Point(200, 170))
    newGameButton.setFill(color_rgb(116, 200, 232))
    newGameButton.setOutline(color_rgb(116, 200, 232))
    newGameButton.draw(win)
    newGame = Text(Point(129, 155), "NEW GAME")
    newGame.setStyle("bold")
    newGame.setSize(12)
    newGame.draw(win)
    #Human button
    humanButton = Rectangle(Point(58, 180), Point(200, 210))
    humanButton.setFill(color_rgb(241, 241, 241))
    humanButton.setOutline(color_rgb(241, 241, 241))
    humanButton.draw(win)
    human = Text(Point(129, 195), "HUMAN")
    human.setStyle("bold")
    human.setSize(12)
    human.setTextColor(color_rgb(241, 241, 241))
    human.draw(win)
    #Computer button
    computerButton = Rectangle(Point(58, 220), Point(200, 250))
    computerButton.setFill(color_rgb(241, 241, 241))
    computerButton.setOutline(color_rgb(241, 241, 241))
    computerButton.draw(win)
    computer = Text(Point(129, 235), "COMPUTER")
    computer.setStyle("bold")
    computer.setSize(12)
    computer.setTextColor(color_rgb(241, 241, 241))
    computer.draw(win)
    #Quit button
    quitButton = Rectangle(Point(58, 400), Point(200, 430))
    quitButton.setFill(color_rgb(107, 13, 13))
    quitButton.setOutline(color_rgb(107, 13, 13))
    quitButton.draw(win)
    quitText = Text(Point(129, 415), "QUIT")
    quitText.setStyle("bold")
    quitText.setSize(12)
    quitText.setTextColor("white")
    quitText.draw(win)
    return quitButton, score, scoreVal, status, newGameButton, humanButton, computerButton, human, computer

# makeBoardInterface function will create and draw the boxes for the game board.
# The function will return boxes that can be used to play the game.
# Input parameter: graphics window (win)
# Output parameters: the variable names for each box is the following box[row][column]
# box0102, box0103, box0104 = Boxes that can be used for moving up
# box0201, box0301, box0401 = Boxes that can be used for moving left
# box0205, box0305, box0405 = Boxes that can be used for moving right
# box0502, box0503, box0504 = Boxes that can be used for moving down
def makeBoardInterface(win):
    # Creates the first row
    box0101 = Rectangle(Point(300, 140), Point(350, 190))
    box0101.setFill(color_rgb(210, 218, 225))
    box0101.setOutline(color_rgb(210, 218, 225))
    box0101.draw(win)
    box0102 = Rectangle(Point(360, 140), Point(410, 190))
    box0102.setFill(color_rgb(210, 218, 225))
    box0102.setOutline(color_rgb(210, 218, 225))
    box0102.draw(win)
    box0103 = Rectangle(Point(420, 140), Point(470, 190))
    box0103.setFill(color_rgb(210, 218, 225))
    box0103.setOutline(color_rgb(210, 218, 225))
    box0103.draw(win)
    box0104 = Rectangle(Point(480, 140), Point(530, 190))
    box0104.setFill(color_rgb(210, 218, 225))
    box0104.setOutline(color_rgb(210, 218, 225))
    box0104.draw(win)
    box0105 = Rectangle(Point(540, 140), Point(590, 190))
    box0105.setFill(color_rgb(210, 218, 225))
    box0105.setOutline(color_rgb(210, 218, 225))
    box0105.draw(win)
    
    # Creates the second row
    box0201 = Rectangle(Point(300, 200), Point(350, 250))
    box0201.setFill(color_rgb(210, 218, 225))
    box0201.setOutline(color_rgb(210, 218, 225))
    box0201.draw(win)
    box0202 = Rectangle(Point(360, 200), Point(410, 250))
    box0202.setFill(color_rgb(210, 218, 225))
    box0202.setOutline(color_rgb(210, 218, 225))
    box0202.draw(win)
    box0203 = Rectangle(Point(420, 200), Point(470, 250))
    box0203.setFill(color_rgb(210, 218, 225))
    box0203.setOutline(color_rgb(210, 218, 225))
    box0203.draw(win)
    box0204 = Rectangle(Point(480, 200), Point(530, 250))
    box0204.setFill(color_rgb(210, 218, 225))
    box0204.setOutline(color_rgb(210, 218, 225))
    box0204.draw(win)
    box0205 = Rectangle(Point(540, 200), Point(590, 250))
    box0205.setFill(color_rgb(210, 218, 225))
    box0205.setOutline(color_rgb(210, 218, 225))
    box0205.draw(win)

    # Creates the third row
    box0301 = Rectangle(Point(300, 260), Point(350, 310))
    box0301.setFill(color_rgb(210, 218, 225))
    box0301.setOutline(color_rgb(210, 218, 225))
    box0301.draw(win)
    box0302 = Rectangle(Point(360, 260), Point(410, 310))
    box0302.setFill(color_rgb(210, 218, 225))
    box0302.setOutline(color_rgb(210, 218, 225))
    box0302.draw(win)
    box0303 = Rectangle(Point(420, 260), Point(470, 310))
    box0303.setFill(color_rgb(210, 218, 225))
    box0303.setOutline(color_rgb(210, 218, 225))
    box0303.draw(win)
    box0304 = Rectangle(Point(480, 260), Point(530, 310))
    box0304.setFill(color_rgb(210, 218, 225))
    box0304.setOutline(color_rgb(210, 218, 225))
    box0304.draw(win)
    box0305 = Rectangle(Point(540, 260), Point(590, 310))
    box0305.setFill(color_rgb(210, 218, 225))
    box0305.setOutline(color_rgb(210, 218, 225))
    box0305.draw(win)

    # Creates the fourth row
    box0401 = Rectangle(Point(300, 320), Point(350, 370))
    box0401.setFill(color_rgb(210, 218, 225))
    box0401.setOutline(color_rgb(210, 218, 225))
    box0401.draw(win)
    box0402 = Rectangle(Point(360, 320), Point(410, 370))
    box0402.setFill(color_rgb(210, 218, 225))
    box0402.setOutline(color_rgb(210, 218, 225))
    box0402.draw(win)
    box0403 = Rectangle(Point(420, 320), Point(470, 370))
    box0403.setFill(color_rgb(210, 218, 225))
    box0403.setOutline(color_rgb(210, 218, 225))
    box0403.draw(win)
    box0404 = Rectangle(Point(480, 320), Point(530, 370))
    box0404.setFill(color_rgb(210, 218, 225))
    box0404.setOutline(color_rgb(210, 218, 225))
    box0404.draw(win)
    box0405 = Rectangle(Point(540, 320), Point(590, 370))
    box0405.setFill(color_rgb(210, 218, 225))
    box0405.setOutline(color_rgb(210, 218, 225))
    box0405.draw(win)

    # Creates the fifth row
    box0501 = Rectangle(Point(300, 380), Point(350, 430))
    box0501.setFill(color_rgb(210, 218, 225))
    box0501.setOutline(color_rgb(210, 218, 225))
    box0501.draw(win)
    box0502 = Rectangle(Point(360, 380), Point(410, 430))
    box0502.setFill(color_rgb(210, 218, 225))
    box0502.setOutline(color_rgb(210, 218, 225))
    box0502.draw(win)
    box0503 = Rectangle(Point(420, 380), Point(470, 430))
    box0503.setFill(color_rgb(210, 218, 225))
    box0503.setOutline(color_rgb(210, 218, 225))
    box0503.draw(win)
    box0504 = Rectangle(Point(480, 380), Point(530, 430))
    box0504.setFill(color_rgb(210, 218, 225))
    box0504.setOutline(color_rgb(210, 218, 225))
    box0504.draw(win)
    box0505 = Rectangle(Point(540, 380), Point(590, 430))
    box0505.setFill(color_rgb(210, 218, 225))
    box0505.setOutline(color_rgb(210, 218, 225))
    box0505.draw(win)

    return box0102, box0103, box0104, box0201, box0301, box0401, box0205, box0305, box0405, box0502, box0503, box0504

#---------------SECTION 2. GAME FLOW-------------------
# The following section will control the game flow behind the graphics, such as the algorithms behind each movement.

# createBoard function will create a nested list to be used for the game.
# It will then return both the game board and its columns in the form of a nested list.
# The nested list will all contain the value zero in this function.
# Input parameter: none
# Output parameters:
# - nested list for game board (gameBoard)
# - the list of columns in the form of a nested list (gameColumns)
def createBoard():
    gameColumns = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    gameColumns = [list(i) for i in gameColumns]
    gameBoard = [list(i) for i in (zip(*gameColumns))]
    return gameBoard, gameColumns

# fillDefault function will randomly fill in the game board with default values (tiles containing value 2).
# It randommly generate how many new tiles should be inserted (values).
# It wil use a loop for the length of values to randomly generate a position for the new tile.
# Then, the value at that position will be changed to be equal to two.
# Input parameters: empty board (board), empty column (col)
# Output parameters: filled in board (board), filled in columns (col)
def fillDefault(board, col):
    values = randrange(1, 26)
    for i in range (1, values + 1):
        positionRow = randrange(0, 5)
        positionColumn = randrange(0, 5)
        board[positionRow][positionColumn] = 2
        col[positionColumn][positionRow] = 2
    for row in range(len(col)):
        col[row].reverse()
    return board, col

# slideUp function will move up all the values in the board to the very top position.
# In each column, it will check for any value that is equal to zero.
# For each zero value, it will check the rest of the column for values bigger than zero.
# If found, the row for zero value will be set to be equal to row for value bigger than 0.
# The latter row will be set to zero.
# The list of columns will then be read and returned as a board (board).
# Input parameters: current board (board), current column (col)
# Output parameters: modified board (board), modified column (col)
def slideUp(board, col):
    for colVal in range(len(col)):
        for row in range(len(col[colVal])):
            if col[colVal][row] == 0:
                for check in range(row+1,5):
                    if col[colVal][check] > 0:
                        col[colVal][row], col[colVal][check] = col[colVal][check], 0
                        break
    board = [list(i) for i in (zip(*col))]
    return board, col

# moveUp function will move up all the values and add all adjacent values in the board to the very top position and .
# It will first call the slideUp function and slides all the values to the top of the board.
# Then, for each column, it checks one row with the next to see if the value is equal.
# If yes, the value is added to the earlier row, and the latter row is set to zero.
# slideUp is then called again to make sure all values moves to the top.
# Input parameters: slideUp function, current board (board), current column (col)
# Output parameters: modified board (board), modified column (col)
def moveUp(slideUp, board, col):
    slideUp(board, col)
    for colVal in range(len(col)):
        for row in range(len(col[colVal])-1):
            if col[colVal][row] == col[colVal][row+1]:
                col[colVal][row], col[colVal][row+1] = 2*(col[colVal][row]), 0
    board = [list(i) for i in (zip(*col))]
    board, col = slideUp(board, col)
    return board, col

# rotateClockwise function will rotate the game board in a clockwise direction.
# This will read each column of the board and output it as the board's row.
# The nested list col will then be updated according to the game board.
# Input parameters: current board (board), current column (col)
# Output parameters: modified board (board), modified column (col)
def rotateClockwise(board, col):
    board = [list(i) for i in (zip(*board))]
    for row in range(len(board)):
        board[row].reverse()
    col = [list(i) for i in (zip(*board))]
    return board, col

# rotateAntiClockwise function will rotate the game board in an anti-clockwise direction.
# It will call the rotateClockwise function 3 times, and update the board and its columns accordingly.
# Input parameters: rotateClockwise function, current board (board), current column (col)
# Output parameters: modified board (board), modified column (col)
def rotateAntiClockwise(rotateClockwise, board, col):
    board, col = rotateClockwise(board, col)
    board, col = rotateClockwise(board, col)
    board, col = rotateClockwise(board, col)
    return board, col

# moveLeft function will move all the values left and adds identical adjacent tiles in the left direction.
# It will rotate the board clockwise, moves up all the values, and rotates it back anti-clockwise.
# The board and its columns will be updated accordingly.
# Input parameters: moveUp function, rotateClockwise function, rotateAntiClockwise function, current board (board), current column (col)
# Output parameters: modified board (board), modified column (col)
def moveLeft(moveUp, rotateClockwise, rotateAntiClockwise, board, col):
    board, col = rotateClockwise(board, col)
    board, col = moveUp(slideUp, board, col)
    board, col = rotateAntiClockwise(rotateClockwise, board, col)
    return board, col

# moveRight function will move all the values right and adds identical adjacent tiles in the right direction.
# It will rotate the board anti-clockwise, moves up all the values, and rotates it back clockwise.
# The board and its columns will be updated accordingly.
# Input parameters: moveUp function, rotateClockwise function, rotateAntiClockwise function, current board (board), current column (col)
# Output parameters: modified board (board), modified column (col)
def moveRight(moveUp, rotateClockwise, rotateAntiClockwise, board, col):
    board, col = rotateAntiClockwise(rotateClockwise, board, col)
    board, col = moveUp(slideUp, board, col)
    board, col = rotateClockwise(board, col)
    return board, col

# moveDown function will move all the values down and adds identical adjacent tiles in the downwards direction.
# It will rotate the board clockwise 3 times, moves up all the values, and rotates it back anti-clockwise 2 times.
# The board and its columns will be updated accordingly.
# Input parameters: moveUp function, rotateClockwise function, rotateAntiClockwise function, current board (board), current column (col)
# Output parameters: modified board (board), modified column (col)
def moveDown(moveUp, rotateClockwise, rotateAntiClockwise, board, col):
    board, col = rotateClockwise(board, col)
    board, col = rotateClockwise(board, col)
    board, col = moveUp(slideUp, board, col)
    board, col = rotateAntiClockwise(rotateClockwise, board, col)
    board, col = rotateAntiClockwise(rotateClockwise, board, col)
    return board, col

# addNew function will add a new tile to the board, where its position will depend on the player's move.
# For the corresponding move, it will check each value of each row in the board if it is equal to zero.
# If it is zero, the new tile will be added there. If not, it will search for the next available position.
# The searching algorithm is different for each move, so the new tile can be inserted at the appropriate position.
# Input parameters: player move inputted as text (move), current board (board), current column (col)
# Output parameters: modified board (board), modified column (col)
def addNew(move, board, col):
    newRow = -1
    newCol = -1
    if move == moveUp:
        newVal = False
        for row in range(len(board)-1, -1, -1):
            for i in range(len(board[row])-1, -1, -1):
                if board[row][i] == 0:
                    board[row][i] = 2
                    newVal = True
                    newRow, newCol = row, i
                    break
            if newVal == True:
                break
            
    elif move == moveDown:
        newVal = False
        for row in range(len(board)):
            for i in range(len(board[row])):
                if board[row][i] == 0:
                    board[row][i] = 2
                    newVal = True
                    newRow, newCol = row, i
                    break
            if newVal == True:
                break
            
    elif move == moveLeft:
        newVal = False
        for row in range(len(board)):
            for i in range(len(board[row])-1, -1, -1):
                if board[row][i] == 0:
                    board[row][i] = 2
                    newVal = True
                    newRow, newCol = row, i
                    break
            if newVal == True:
                break

    elif move == moveRight:
        newVal = False
        for row in range(len(board)-1, -1, -1):
            for i in range(len(board[row])):
                if board[row][i] == 0:
                    board[row][i] = 2
                    newVal = True
                    newRow, newCol = row, i
                    break
            if newVal == True:
                break
            
    col = [list(i) for i in (zip(*board))]
    return board, col, newRow, newCol

# randomMove function will randomly generate a number between 1 and 4.
# Each number has been associated with a possible move.
# It will then return the move the computer should make.
# Input parameters: none
# Output parameters: move to be made in string format (move)
def randomMove():
    selectMove = randrange(1,5)
    if selectMove == 1:
        move = "up"
    if selectMove == 2:
        move = "down"
    elif selectMove == 3:
        move = "left"
    elif selectMove == 4:
        move = "right"
    return move

# isLegal function will check the current board and its copy before a move is made.
# If any changes are found, it will return True, meaning the move was legal and successful.
# If changes are not found, it will return False, meaning the move was not successful.
# Input parameters: current board (revisedBoard), its copy (checkBoard)
# Ouput parameters: successful move or not (True or False)
def isLegal(checkBoard, revisedBoard):
    if checkBoard != revisedBoard:
        return True
    else:
        return False

# clicked function will check if the user click is inside a certain button.
# It will get the X and Y coordinate of the click, and check if that coordinate is inside the button area.
# Input parameters: userClick and button
# Output parameters: button clicked or not (True or False)
def clicked(userClick, button):
    clickX = userClick.getX()
    clickY = userClick.getY()
    rectLeft = button.getP1()
    leftPointX = rectLeft.getX()
    leftPointY = rectLeft.getY()
    rectRight = button.getP2()
    rightPointX = rectRight.getX()
    rightPointY = rectRight.getY()
    if leftPointX <= clickX <= rightPointX and leftPointY <= clickY <= rightPointY:
        return True

# gameOver function will check the board if any legal moves are still possible.
# It will first check if the board has any empty spaces left or not.
# If it is completely full, it will then check if there are any adjacent values in the rows and columns.
# Then, if no adjacent values are found, it will return True for game over. Otherwise, it returns False.
# Input parameters: current board (board), current columns (col)
# Output parameters: game over or not (True or False)
def gameOver(board, col):
    gameOver = False
    full = []
    adjacent = []
    for row in range(len(board)):
        for i in range(len(board[row])):
            if board[row][i] == 0:
                full.append(board[row][i])
    if len(full) > 0:
        return False
    elif len(full) == 0:
        for row in range(len(board)):
            for i in range(len(board[row])-1):
                if board[row][i] == board[row][i+1]:
                    adjacent.append(board[row][i])
        for colVal in range(len(col)):
            for row in range(len(col[colVal])-1):
                if col[colVal][row] == col[colVal][row+1]:
                    adjacent.append(col[colVal][row])
        if len(adjacent) > 0:
            return False
        else:
            return True

#---------------SECTION 3. UPDATES DISPLAY-------------------
# The following section will control the display of the game board.

# drawBoardInterface function will take the nested list and display it on the game window.
# For any values that equals to zero, the text color is set to be the same as the background.
# A current version of the board and a copy of the board before a move is made will be checked for changes.
# Any changes found, where the new value is NOT zero, will be shown in the board in red.
# Any new tiles generated because of a move will also be shown in red.
# Otherwise, the tile's value is set to default colour, black.
# Each Text object for the board value will also be added to a list.
# Input parameters: game window (win), copy of board before a move is made (checkedBoard), current version of the board (movedBoard), position of the new tile (newRow, newCol)
# Output parameters: list of Text objects of board value (boardVal)
def drawBoardInterface(win, checkedBoard, movedBoard, newRow, newCol):
    posX = 325
    posY = 165
    boardVal = []
    for row in range(len(movedBoard)):
        for i in range(len(movedBoard[row])):
            val = Text(Point(posX, posY), str(movedBoard[row][i]))
            val.setStyle("bold")
            val.setSize(16)
            if movedBoard[row][i] == 0:
                val.setTextColor(color_rgb(210, 218, 225))
            elif movedBoard[row][i] != 0 and movedBoard[row][i] != checkedBoard[row][i]:
                val.setTextColor(color_rgb(30,144,255))
            elif row == newRow and i == newCol:
                val.setTextColor(color_rgb(30,144,255))
            val.draw(win)
            boardVal.append(val)
            posX += 60
        posX = 325
        posY += 60
    return boardVal

# eraseBoardInterface function will undraw each Text object in the list of Text objects of board value.
# Input parameter: list of Text objects of board value (boardVal)
# Output parameter: none
def eraseBoardInterface(boardVal):
    for i in boardVal:
        i.undraw()

# updateScore function will update the score value according to whether a move was successful or not.
# The score value will then be displayed on the score board.
# Input parameters: current score value (scoreVal), Text object for score board (score), change to be applied to score - add one or subtract one (change)
# Output parameter: current score value (scoreVal)
def updateScore(scoreVal, score, change):
    scoreVal += change
    score.setText(str(scoreVal))
    return scoreVal

# This will run the main function each time the code is run.
main()

