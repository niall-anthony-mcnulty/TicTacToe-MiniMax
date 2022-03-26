import random as random



board = {1: ' ',2: ' ', 3: ' ',
         4: ' ',5: ' ', 6: ' ',  
         7: ' ',8: ' ', 9: ' ',}

        
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("-+-+-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-+-+-")
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-+-+-")
    print("\n")



def spaceIsFree(position):

    if(board[position]== ' '):
        return True
    else:
        return False


def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True

    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True

    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True

    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True

    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    
    else:
        return False


def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True

    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True

    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True

    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True

    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    
    else:
        return False

def checkForDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)

        if (checkForWin()):
            if letter == player:
                print('Player wins!')
                exit()
            else:
                print('The bot wins!')
                exit()

        if (checkForDraw()):
            print("Draw!")
            exit()

    
    else:
        if letter == player:
            print("That space is already played, try another!")
            position = int(input("Enter a new position: "))
            insertLetter(letter,position)
            return
        else:
            position = int(random.randint(0,10))
            insertLetter(letter,position)
            return


def playerMove(letter):
    position = int(input(f'Enter a board position: '))
    insertLetter(letter, position)
    return


def botMove(letter):
    if easyOrHard == 'N':
        position = int(random.randint(0,10))
        insertLetter(letter, position)
        

    else:
        if easyOrHard == 'Y':
            bestScore = -1000
            bestMove = 0
            for key in board.keys():
                if (board[key]== ' '):
                    board[key] = bot
                    score = minimax(board, 0, False)
                    board[key] = ' '
                    if (score > bestScore):
                
                        bestScore = score      
                        bestMove = key
                       
            
            insertLetter(bot, bestMove)
            return


def minimax(board, depth, isMaximizing):
    
    if checkWhichMarkWon(bot):
        return 100
    elif checkWhichMarkWon(player):
        return -100
    elif checkForDraw():
        return 0

    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if (board[key]== ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score   
        return bestScore

    
    else:

        bestScore = 1000
        for key in board.keys():
            if (board[key]== ' '):
                board[key] = player
                score = minimax(board, depth + 1,  True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score        
        return bestScore





def main():
    # choosing whether to play against a bot with random generated picks or using the the minimax algorithm
    global easyOrHard
    easyOrHard = str(input("Enter 'y' for GOD-MODE or 'n' for SIMP-MODE:   ")).upper()
    print("\n\n")
    while (easyOrHard != 'Y') and (easyOrHard != 'N'):
        easyOrHard = str(input("Please make sure to type 'y' for GOD-MODE  or 'n' for SIMP-MODE when choosing your difficulty:  ")).upper()
        print("\n\n")
    # choosing whether to play with the X or Y
    global player
    player = str(input("Select whether to play with 'X' or 'O' to start the game:  "))
    print("\n\n")
    print("\n\n")
    player = player.upper()
    global bot
    while (player != 'X') and (player != 'O'):
        print("You did not enter an X or O, please try again!")
        print("\n\n")
        print("\n\n")
        player = str(input("Select whether to play with 'X' or 'O' to start the game:  "))
        print("\n\n")
        print("\n\n")
        player = player.upper()
        
    if player == 'X':
        bot = 'O'
    else:
        if player == 'O':
            bot = 'X'
        
    print(f"Player has chosen {player}. Play your first move.. Good luck! \n\n" )
    
    while not checkForWin():
        printBoard(board)
        playerMove(player)
        botMove(bot)

    exit()
        

main()