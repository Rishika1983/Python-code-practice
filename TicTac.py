# Game of tic tac

'''This function is to ask the player to choose their position.
alreadyfilled boolean tell this function that position is already filled,
so ask the player to input another position'''
def playerposition(marker,alreadyfilled):
    stragain = ''
    if alreadyfilled:
        stragain=' again'
    if marker.upper()=='X':
        position=input('player 1 (X)enter your position from 1-9'+stragain)
    else:
        position=input('player 2 (O)enter your position from 1-9'+stragain)
    print(position)
    return(position)

#To check empty space in the board
def spacecheck(board):
    space=False
    for x in range(1,10):
        if board[x]==' ':
            space=True
            break
    return space

#To display tic tac board on screen
def display_board(position):
    #faking clear screen
    print('\n'*80)
    print(position[7] + '|' + position[8] + '|' + position[9])
    print(position[4] + '|' + position[5] + '|' + position[6])
    print(position[1] + '|' + position[2] + '|' + position[3])



def result(markerplace):
    print('result')
    # these are the posible positions to win the game
    resultset = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1]]
    #print(markerplace)
    # xpos will collect all the X positions on the board
    xpos = [int(x) for x in markerplace.keys() if markerplace[x] == 'X']
    # opos will collect all the O positions on the board
    opos = [int(x) for x in markerplace.keys() if markerplace[x] == 'O']
    #print(xpos)
    isdraw=True
    # this for loop will iterate all the elements of resultsets
    for x in resultset:
        # if element of resultset is in xpos then X player is the winner
        if all(elem in xpos for elem in x):
            print('Player1 is the winner')
            isdraw=False
            break
        # if element of resultset is in opos then O player is the winner
        elif all(elem in opos for elem in x):
            print('Player2 is the winner')
            isdraw = False
            break
    return isdraw

# main program starting
print('Welcome to TicTac game')
startoption= input('Do you want to be X or O')
player1=False
player2=False
if startoption.upper()=='X':
    player1=True
else:
    player2=True
'''
filledplaces=['%',' ',' ',' ',' ',' ',' ',' ',' ',' ']
enteredoptions=filledplaces 
'''
enteredoptions=['%',' ',' ',' ',' ',' ',' ',' ',' ',' ']
alreadyfilled=False
markerplace={}
playagain=False

while spacecheck(enteredoptions) or playagain:
    display_board(enteredoptions)
    if player1:
        position=playerposition('X',alreadyfilled)
        boardplace=int(position)
        if enteredoptions[boardplace]!=' ':
            player1=True
            alreadyfilled=True
        else:
            enteredoptions[boardplace] ='X'
            markerplace.update({position:'X'})
            player1=False
            alreadyfilled=False
    else:
        #boardplace = int(playerposition('O'))
        position = playerposition('O',alreadyfilled)
        boardplace = int(position)
        if enteredoptions[boardplace]!=' ':
            player1=False
            alreadyfilled=True
        else:
            enteredoptions[boardplace] = 'O'
            markerplace.update({position: 'O'})
            player1=True
            alreadyfilled=False

    if not spacecheck(enteredoptions):
        display_board(enteredoptions)
        if result(markerplace):
            print('It is a draw')
        if input('Do you want to play again?Y/N').upper() == 'Y':
            playagain=True
            enteredoptions=['%',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            print(enteredoptions)

        else:
            playagain=False


