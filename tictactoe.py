# started at 10:30am on 8/3/2023

from random import randint

'''
Okay, so I'm going to try to make a tic tac toe game in python. I think I will use a 2d array  to represent the board. I'll also make a list of players, the first one being the player (X) and the second one being the computer (O).
'''

blank_array = [['_','_','_'],['_','_','_'],['_','_','_']]
array = blank_array.copy()
players = ['X','O']
          
'''
I'm gonna have a function that prints the board, a function that checks if the player has won, and a function that checks if there is a tie.
'''

def printBoard():
    for i in range(3):
        for j in range(3):
            print(array[i][j] + " ", end = "")
        print()

    ### version 2
    # print(f'{array[0][0]}|{array[0][1]}|{array[0][2]}')
    # print(f'{array[1][0]}|{array[1][1]}|{array[1][2]}')
    # print(f'{array[2][0]}|{array[2][1]}|{array[2][2]}')

    ### version 1
    # print(array[0])
    # print(array[1])
    # print(array[2])

'''
Simple enough. I might come back and fix up the formatting later, but for now, this is fine. I'll make the win and tie funcions.
'''

def checkWin(player):
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
    # if all spaces are filled
    if '_' not in array[0] and '_' not in array[1] and '_' not in array[2]:
        return True
    return False

# def checkResult():
#     for player in players:
#         if checkWin(player):
#             return player
#     if checkTie():
#         return 'Tie'
#     return None

'''
Now, I need a function that updates the board. I'll also make the player and computer turn functions and a function that allows the player to play the game again.
'''

def updateBoard(player, guess):
    array[guess[0]][guess[1]] = player
    return array

def takePlayerTurn():
    while True:
        try:
            guess = input('Your turn! Enter your guess: ')
            guess = guess.split(',')
            guess = [int(guess[0]), int(guess[1])]
            if array[guess[0]][guess[1]] == '_':
                updateBoard(players[0], guess)
                break
            else:
                print('That space is already taken. Try again.')
        except ValueError:
            print('Invalid input. Try again.')

def takeComputerTurn():
    print('The computer\'s turn!')
    while True:
        guess = [randint(0,2), randint(0,2)]
        if array[guess[0]][guess[1]] == '_':
            updateBoard(players[1], guess)
            break

def endGame():
    while True:
        play_again = input('Would you like to play again? (y/n) ')
        if play_again == 'y':
            global array
            array = blank_array.copy()
            playGame()
        elif play_again == 'n':
            print('Thanks for playing!')
            exit()
        else:
            print('Invalid input. Try again.')

'''
Cool! Now I just need to make a function that plays the game.
'''

def playGame():
    print('Welcome to Tic Tac Toe!')
    print('You are X, and the computer is O.')
    print('To play, enter the row and column of the space you want to play in.')
    print('The top left space is 0,0, and the bottom right space is 2,2.')
    print('Good luck!')

    player_first = input('Would you like to go first? (y/n) ')
    if player_first == 'y':
        print('You will go first.')
    elif player_first == 'n':
        print('The computer will go first.')
    else:
        print('Invalid input. Try again.')

    printBoard()

    if player_first == 'y':
        while True:
            # player turn
            takePlayerTurn()
            printBoard()
            if checkWin(players[0]):
                print('You win!')
                endGame()
                break
            if checkTie():
                print('It\'s a tie!')
                endGame()
                break
            # computer turn
            takeComputerTurn()
            printBoard()
            if checkWin(players[1]):
                print('You lose!')
                endGame()
                break
            if checkTie():
                print('It\'s a tie!')
                endGame()
                break
    else:
        while True:
            # computer turn
            takeComputerTurn()
            printBoard()
            if checkWin(players[1]):
                print('You lose!')
                endGame()
                break
            if checkTie():
                print('It\'s a tie!')
                endGame()
                break
            # player turn
            takePlayerTurn()
            printBoard()
            if checkWin(players[0]):
                print('You win!')
                endGame()
                break
            if checkTie():
                print('It\'s a tie!')
                endGame()
                break

def main():
    ### win tests
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