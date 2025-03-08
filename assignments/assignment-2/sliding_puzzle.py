#Feodor Gornostayev, 2442384

import random
import sys

def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

def titleLabels(n):
    side_values = []
    for i in range(1, n * n):
        side_values.append(i)
    side_values.append('  ')
    return side_values

def getNewPuzzle(n):
    labels = titleLabels(n)
    random.shuffle(labels)
    board = [ labels[n*i:n*(i+1)] for i in range(0, n)]
    return board

def findEmptyTile(board):
    for row, sublist in enumerate(board):
        for column, element in enumerate(sublist):
            if element == '  ':
                return (row, column)

def nextMove(board):
    n = len(board[0])
    empty_position = findEmptyTile(board)
    down_possibility = empty_position[0] != len(board) - 1 
    up_possibility = empty_position[0] != 0  
    right_possibility = empty_position[1] != len(board[0]) - 1
    left_possibility = empty_position[1] != 0
    
    valid_input = False
    while not valid_input:
        print("                        \t", end='')
        print('  (W)  ' if down_possibility else '  ( )  ')
        print("Enter WASD (or QUIT): \t", end='')
        print('(A)\t' if right_possibility else '  ( )  \t', end='')
        print('  (S)  \t' if up_possibility else '  ( )  \t', end='')
        print('  (D)  ' if left_possibility else '  ( )  ')
        next_move = input().lower()

        if next_move == 'quit':
            sys.exit()
        elif next_move == 'w' and down_possibility:
            valid_input = True
        elif next_move == 's' and up_possibility:
            valid_input = True
        elif next_move == 'a' and right_possibility:
            valid_input = True
        elif next_move == 'd' and left_possibility:
            valid_input = True

    return next_move


def makeMove(board, next_move):
    empty_position = findEmptyTile(board)
    row, col = empty_position
    
    #Fixed to work with logic in instructions (mixed up w with s and a with d)
    if next_move == 'w' and row < len(board) - 1:  
        board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
    elif next_move == 's' and row > 0:  
        board[row][col], board[row - 1][col] = board[row - 1][col], board[row][col]
    elif next_move == 'a' and col < len(board[0]) - 1: 
        board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]
    elif next_move == 'd' and col > 0:  
        board[row][col], board[row][col - 1] = board[row][col - 1], board[row][col]
    
    return board

def verifyWin(board):
    n = len(board)
    for i in range(n):
        for j in range(n - 1):
            if board[i][j] != '  ' and board[i][j + 1] != '  ' and int(board[i][j]) > int(board[i][j + 1]):
                return False
    for j in range(n):
        for i in range(n - 1):
            if board[i][j] != '  ' and board[i + 1][j] != '  ' and int(board[i][j]) > int(board[i + 1][j]):
                return False
    return True


print("Welcome to the Sliding Puzzle Game! The aim of the game is to arrange all the tiles in the puzzle \nto be in increasing order both horizentaly and verticaly\n")
dimension_value = int(input("What should be the side dimension of the square puzzle? (3 or 4): "))
board = getNewPuzzle(dimension_value)
#I might of misundertood, but are we asked to only do the game for 3 of 4 side tiles since those are the only ones given with turn limits?
if dimension_value == 3:
    duration_turns = 31
else:
    duration_turns = 80

for i in range(1, duration_turns):    
    displayBoard(board)
    print(f"Move {i}/{duration_turns}")
    move = nextMove(board)
    board = makeMove(board, move)
    
    if verifyWin(board):
        print(f"You've managed to allign the baord in {i}/{duration_turns}, congratulations!")
        sys.exit()

print(f"The board was not put in order in {duration_turns} moves")
print("Best of luck next time!")

'''
#For running tests
board = getNewPuzzle(3)
displayBoard(board)
nextMove(board)
'''










            