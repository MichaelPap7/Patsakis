import random

def makeb(board):#Συνάρτηση που φτιάχνει τον πίνακα της τρίλιζας
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def playagain():#Συνάρτηση που ελέγχει αν ο χρήστης θέλει να παίξει ξανά
    print("Game Over... Play Again? (y/n)")
    return input().lower().startswith('y')

def winner(board, letter):#Συνάρτηση που ελέγχει τον νικιτή
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or 
            (board[4] == letter and board[5] == letter and board[6] == letter) or 
            (board[7] == letter and board[8] == letter and board[9] == letter) or 
            (board[1] == letter and board[4] == letter and board[7] == letter) or 
            (board[2] == letter and board[5] == letter and board[8] == letter) or 
            (board[3] == letter and board[6] == letter and board[9] == letter) or 
            (board[1] == letter and board[5] == letter and board[9] == letter) or 
            (board[7] == letter and board[5] == letter and board[3] == letter))

def move(board,letter,pos):
    board[pos]=letter

def spacefree(board,pos):#Συνάρτηση που ελέγχει αν η θέση στην οποία θέλει να κάνει κίνηση ο χρήστης είναι κενή
    if board[pos] == ' ':
        return True
    else:
        return False

def playermove(board):#Συνάρτηση κίνησης του χρήστη
    pos=' '
    while pos not in '1,2,3,4,5,6,7,8,9'.split(",") or spacefree(board, int(pos)) is False:
        print('Enter next move (1-9)')
        pos=input()
    return int(pos)

def boardfull(board):#Συνάρτηση που ελέγχει αν ο πίνακας είναι γεμάτος
    for i in range(1, 10):
        if spacefree(board, i):
            return False
        
    return True

def computermove(board):
    pos = random.randint(0, 9)
    while spacefree(board, pos) is False:
	    pos=random.randint(0, 9)

    return int(pos)
	
while True:#Φτιάχνεται/επαναφέρεται ο πίνακας
    board = [' '] * 10
    gameplay = True
    print('You are X. You play first')
    turn='player'
    completter='O'
    playerletter='X'

    while gameplay:#Παίζει ο χρήστης
        if turn == 'player':
			
            makeb(board)
            pos = playermove(board)
            move(board, playerletter, pos)

            if winner(board, playerletter):
                makeb(board)
                print('You have won the game!')
                gameplay = False
            else:
                if boardfull(board):
                    makeb(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:		
            pos = computermove(board)
            move(board, completter, pos)

            if winner(board, completter):
                makeb(board)
                print('You lost.')
                gameplay = False
            else:
                if boardfull(board):
                    makeb(board)
                    print('Draw.')
                    break
                else:
                    turn = 'player'

    if not playagain():
        break
