def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
return ((board['top-L']== player and board['top-M']== player and board['top-R']== player) or
        (board['mid-L']== player and board['mid-M']== player and board['mid-R']== player) or
        (board['low-L']== player and board['low-M']== player and board['low-R']== player) or
        (board['low-L']== player and board['mid-M']== player and board['top-R']== player) or
        (board['top-L']== player and board['mid-M']== player and board['low-R']== player) or
        (board['top-L']== player and board['mid-L']== player and board['low-L']== player) or
        (board['top-M']== player and board['mid-M']== player and board['low-M']== player) or
        (board['top-R']== player and board['mid-R']== player and board['low-R']== player))

def startGame(startingPlayer, board):

    turn = startingPlayer #start of game
    for i in range(9):
        printBoard(board) #Prints board with start of game
        print('Turn for ' + turn + '. Move on which space?') #program asks which space user will like to chose
        move = input()
        board[move] = turn
        if( checkWinner(board, 'X') ): #checks if x has won
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ): #checks if O has won
            print('O wins!')
            break
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board) #reprint board
    