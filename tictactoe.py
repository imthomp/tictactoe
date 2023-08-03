# started at 10:30am on 8/3/2023

from random import randint

'''
Okay, so I'm going to try to make a tic tac toe game in python. I think I will use a 2d array  to represent the board. I'll also make a list of players, the first one being the player (X) and the second one being the computer (O).
'''

blank_array = [['_','_','_'],['_','_','_'],['_','_','_']]
players = ['X','O']
          
'''
I'm gonna have a function that prints the board, a function that checks if the player has won, and a function that checks if there is a tie.
'''

def printBoard(array):
    print(array[0])
    print(array[1])
    print(array[2])

'''
Simple enough. I might come back and fix up the formatting later, but for now, this is fine. I'll make the win and tie funcions.
'''

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

def checkTie(array):
    # if all spaces are filled
    if '_' not in array[0] and '_' not in array[1] and '_' not in array[2]:
        return True

# def checkResult():
#     for player in players:
#         if checkWin(player):
#             return player
#     if checkTie():
#         return 'Tie'
#     return None

'''
Now, I need a function that updates the board. I'll also make the player and computer turn functions.
'''

def updateBoard(array, player, guess):
    array[guess[0]][guess[1]] = player
    return array

def takePlayerTurn():
    while True:
        guess = input('Your turn! Enter your guess: ')
        guess = guess.split(',')
        guess = [int(guess[0]), int(guess[1])]
        if blank_array[guess[0]][guess[1]] == '_':
            blank_array[guess[0]][guess[1]] = players[0]
            break
        else:
            print('That space is already taken. Try again.')
    return blank_array

def takeComputerTurn():
    print('The computer\'s turn!')
    while True:
        guess = [randint(0,2), randint(0,2)]
        if blank_array[guess[0]][guess[1]] == '_':
            blank_array[guess[0]][guess[1]] = players[1]
            break
    return blank_array

'''
Cool! Now I just need to make a function that plays the game.
'''

def playGame():
    print('Welcome to Tic Tac Toe!')
    print('You are X, and the computer is O.')
    print('To play, enter the row and column of the space you want to play in.')
    print('The top left space is 0,0, and the bottom right space is 2,2.')
    print('Good luck!')
    printBoard(blank_array)
    while True:
        # player turn
        takePlayerTurn()
        printBoard(blank_array)
        if checkWin(blank_array, players[0]):
            print('You win!')
            break
        if checkTie(blank_array):
            print('It\'s a tie!')
            break
        # computer turn
        takeComputerTurn()
        printBoard(blank_array)
        if checkWin(blank_array, players[1]):
            print('You lose!')
            break
        if checkTie(blank_array):
            print('It\'s a tie!')
            break

def main():
    # game1 = [['X','X','X'],['_', '_', '_'], ['_', '_', '_']]
    # print(checkWin(game1, 'X'))
    # game2 = [['X','_','_'],['_', 'X', '_'], ['_', '_', 'X']]
    # print(checkWin(game2, 'X'))
    # game3 = [['_','O','_'],['_', 'O', '_'], ['_', 'O', '_']]
    # print(checkWin(game3, 'O'))
    # game4 = [['_','_','O'],['_', 'O', '_'], ['O', '_', '_']]
    # print(checkWin(game4, 'O'))
    # game5 = [['_','_','O'],['_', 'X', '_'], ['O', '_', '_']]
    # print(checkWin(game5, 'O'))

    playGame()

main()