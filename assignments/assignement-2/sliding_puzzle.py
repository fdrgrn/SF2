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
    #Booleans w, a, s, d (True if you can, False if you can't)
    up_possibility = empty_position[0] != 0
    down_possibility = empty_position[0] != n - 1
    left_possibility = empty_position[1] != 0
    right_possibility = empty_position[1] != n - 1
    
    valid_input = False
    while not valid_input:
        print("                        \t", end = '')
        print('  (W)  ' if up_possibility else '  ( )  ') 
        print("Enter WASD (or QUIT): \t", end = '')
        print('(A)\t' if left_possibility else '  ( )  \t', end = '')
        print('  (S)  \t' if down_possibility else '  ( )  \t', end = '')
        print('  (D)  ' if right_possibility else '  ( )  ')
        input_answer = input().lower()

        if input_answer == 'quit':
            sys.exit()
        elif input_answer == 'w' and up_possibility:
            valid_input = True
        elif input_answer == 's' and down_possibility:
            valid_input = True
        elif input_answer == 'a' and left_possibility:
            valid_input = True
        elif input_answer == 'd' and right_possibility:
            valid_input = True

    return input_answer
'''
#For running tests:
board = getNewPuzzle(3)
displayBoard(board)
nextMove(board)
'''










            
