# started at 10:30am on 8/3/2023

'''
Okay, so I'm going to try to make a tic tac toe game in python. I think I will use a 2d array  to represent the board.
'''

blank_array = [['_','_','_'],['_','_','_'],['_','_','_']]
          
'''
I'm gonna have a function that prints the board, a function that checks if the player (X) has won, and a function that checks if there is a tie. Also, I might as well make a function that plays the game.
'''

def printBoard(array):
    print(array[0])
    print(array[1])
    print(array[2])

'''
Simple enough. I might come back and fix up the formatting later, but for now, this is fine.
'''

players = ['X','O']

def checkWin(array, player):
    for i in range(3):
        # horizontal
        if array[i][0] == array[i][1] == array[i][2] == player:
            return True
        # vertical
        if array[0][i] == array[1][i] == array[2][i] == player:
            return True
    # downward
    if array[0][0] == array[1][1] == array[2][2] == player:
        return True
    # upward
    if array[0][2] == array[1][1] == array[2][0] == player:
        return True
    return False

def checkTie():
    # unimplemented
    return

def playGame():
    # unimplemented
    if checkWin():
        return
    if checkTie():
        return
    return

def main():
    game1 = [['X','X','X'],['_', '_', '_'], ['_', '_', '_']]
    print(checkWin(game1, 'X'))
    game2 = [['X','_','_'],['_', 'X', '_'], ['_', '_', 'X']]
    print(checkWin(game2, 'X'))
    game3 = [['_','O','_'],['_', 'O', '_'], ['_', 'O', '_']]
    print(checkWin(game3, 'O'))
    game4 = [['_','_','O'],['_', 'O', '_'], ['O', '_', '_']]
    print(checkWin(game4, 'O'))
    game5 = [['_','_','O'],['_', 'X', '_'], ['O', '_', '_']]
    print(checkWin(game5, 'O'))

main()