#To run: pip install pysimplegui

import PySimpleGUI as sg

#function to check if a player has won
def check_win(board, player):
    # check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and\
        board[i][2] == player:
            return True
    # check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and\
           board[2][i] == player:
            return True
    # check diagonals
    if board[0][0] == player and board[1][1] == player and\
       board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and\
       board[2][0] == player:
        return True
    return False


#function to check if game is tied
def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


# Main function to play the game
def play_game():
    # Set up GUI
    sg.change_look_and_feel('Dark Blue 3')
    layout = [[sg.Button('', size=(16, 10), key=(i, j), pad=(0, 0))
                         for j in range(3)] for i in range(3)]
    layout.append([sg.Text('Player X turn', size=(20, 1),
                           key='turn')])
    window = sg.Window('Tic-Tac-Toe', layout)
    player = 'X'
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Quit'):
            break
        if event in (None, 'turn'):
            continue
        if board[event[0]][event[1]] != ' ':
            continue
        board[event[0]][event[1]] = player
        window[event].update(player)
        if check_win(board, player):
            sg.popup('Player {} has won!'.format(player))
            break
        if check_tie(board):
            sg.popup("It's a tie!")
            break
        player = 'O' if player == 'X' else 'X'
        window['turn'].update('Player {} turn'.format(player))
    window.close()


play_game()
