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
        printBoard(board)

        if (checkForDraw()):
            print("Draw!")
            exit()
        if (checkForWin()):
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins")
                exit()

    
    else:
        if letter == 'X':
            print("That space is already played, try another!")
            position = int(input("Enter a new position: "))
            insertLetter(letter,position)
            return
        else:
            position = int(random.randint(0,9))
            insertLetter(letter,position)
            return


player = 'O'
bot = 'X'

def playerMove():
    position = int(input("Enter the position for 'O': "))
    insertLetter(player, position)
    return

def botMove():
    position = int(random.randint(0,9))
    insertLetter(bot, position)
    return

while not checkForWin():
    printBoard(board)
    playerMove()
    botMove()


