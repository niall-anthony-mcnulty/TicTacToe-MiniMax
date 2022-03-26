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

def checkForDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter

        if (checkForDraw()):
            print("Draw!")
            exit()
        if (checkForWin()):
            if letter == player:
                print('Player wins!')
                exit()
            else:
                print('The bot wins!')

    
    else:
        if letter == player:
            print("That space is already played, try another!")
            position = int(input("Enter a new position: "))
            insertLetter(letter,position)
            return
        else:
            position = int(random.randint(0,9))
            insertLetter(letter,position)
            return

def playerMove(letter):
    position = int(input(f'Enter a board position: '))
    insertLetter(letter, position)
    return

def botMove(letter):
    position = int(random.randint(0,9))
    insertLetter(letter, position)
    return



def main():
    global player
    player = str(input("Select whether to play with 'X' or 'O' to start the game: "))
    player = player.upper()
    global bot
    bot = str()
    while (player != 'X') and (player != 'O'):
        print("You did not enter an X or O, please try again!")
        player = str(input("Select whether to play with 'X' or 'O' to start the game: "))
        player = player.upper()
        
    if player == 'X':
        bot = 'O'
    else:
        bot = 'X'
        
    print(f"Player has chosen {player}. Play your first move.. Good luck! \n\n" )
    
    while not checkForWin():
        printBoard(board)
        playerMove(player)
        botMove(bot)

    exit()
        

main()