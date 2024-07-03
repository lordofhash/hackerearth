import re
from copy import deepcopy

def retr(column, row, board):
    try:
        value = str(board[column][row])
    except IndexError:
        return ' '
    else:
        return value

def printboard(board):
    print('.---------------------------.')
    for i in range(5, -1, -1):
        print('|', end=' ')
        for j in range(7):
            print(retr(j, i, board) + ' |', end=' ')
        if i > 0:
            print('\n|---------------------------|')
        else:
            print('\n*---------------------------*')
            print('  1   2   3   4   5   6   7')

def row_count(row_or_column):
    teir_list = [
        [["R", "R", "R", "R"], ["R", "R", "R", " "], ["R", "R", " ", "R"], ["R", " ", "R", "R"], [" ", "R", "R", "R"]],
        [["B", "B", "B", "B"], ["B", "B", "B", " "], ["B", "B", " ", "B"], ["B", " ", "B", "B"], [" ", "B", "B", "B"]]
    ]
    counting = []
    for h in range(len(teir_list)):
        for i in range(len(teir_list[h])):
            pattern = ', '.join(teir_list[h][i])
            s = re.findall(pattern, row_or_column)
            if s:
                counting.append([h, i])
    return counting

def num_generate(teirs):
    num = 0
    for i in range(len(teirs)):
        subnum = 0
        if teirs[i][1] == 0:
            subnum = 1000000
        elif teirs[i][1] == 1:
            subnum = 750
        elif teirs[i][1] == 2:
            subnum = 250
        elif teirs[i][1] == 3:
            subnum = 25
        elif teirs[i][1] == 4:
            subnum = 5
        if teirs[i][0] == 0:
            subnum += 1
            subnum *= -1
        num += subnum
    return num

def win(string):
    redwins = "R, R, R, R"
    blackwins = "B, B, B, B"
    if re.findall(redwins, string):
        return True
    elif re.findall(blackwins, string):
        return True
    return False

class TooHigh(Exception):
    pass

def check4stuff(board, use):
    num = 0
    if use == 0:
        if win(str(board)):
            return True
    if use == 1:
        num += num_generate(row_count(str(board)))
    for h in range(3, 9):
        diag = []
        for i in range(h - 5 if h > 5 else 0, 7 if h > 7 else h + 1):
            j = h - i
            if i < 7:
                diag.append(retr(i, j, board))
        if use == 0 and win(str(diag)):
            return True
        if use == 1:
            num += num_generate(row_count(str(diag)))
    for h in range(-3, 3):
        diag = []
        for i in range(abs(h) if h < 0 else 0, 7 - h if h >= 0 else 7):
            j = i + h
            if i < 7:
                diag.append(retr(i, j, board))
        if use == 0 and win(str(diag)):
            return True
        if use == 1:
            num += num_generate(row_count(str(diag)))
    for i in range(6):
        horizontals = [retr(j, i, board) for j in range(7)]
        if use == 0 and win(str(horizontals)):
            return True
        if use == 1:
            num += num_generate(row_count(str(horizontals)))
    return num if use == 1 else False

def find_smlorlrg(scores, func):
    return reduce(func, scores)

def generate_boards(board, color):
    for i in range(7):
        if len(board[i]) < 6:
            new_board = deepcopy(board)
            new_board[i].append(color)
            yield new_board

def minimax(board, depth, turn=0):
    if check4stuff(board, 0):
        return check4stuff(board, 1)
    if turn == depth:
        return check4stuff(board, 1)
    moves = []
    color = 'R' if turn % 2 == 0 else 'B'
    for new_board in generate_boards(board, color):
        score = minimax(new_board, depth, turn + 1)
        moves.append(score)
    return min(moves) if color == 'R' else max(moves)

def full_board(board):
    return all(len(col) >= 6 for col in board)

def get_count():
    while True:
        try:
            players = int(input('How many players? \n(enter 1 or 2): \n'))
            if players in [1, 2]:
                return players
        except ValueError:
            print("Not a number...")

def p_count(board):
    while True:
        try:
            place = int(input('What column would you like to play your piece in?\n'))
            if 1 <= place <= 7:
                if len(board[place - 1]) < 6:
                    return place
                else:
                    raise TooHigh
            else:
                print('Out of range\n')
        except ValueError:
            print('Not a number...\n')
        except TooHigh:
            print('That column is filled\n')

def difficulty():
    while True:
        try:
            input_depth = int(input('What difficulty ? \n*Hit 1 then enter for easy\n*Hit 2 then enter for hard\n*Hit 3 then enter for extremely difficult (only do this if you don\'t mind waiting a bit)\n'))
            if input_depth in [1, 2, 3]:
                return input_depth * 2
            else:
                print('Incorrect Entry...')
        except ValueError:
            print("Not a number...")

def main_game():
    while True:
        board = [[] for _ in range(7)]
        player_count = get_count()
        turn = 0
        if player_count == 1:
            depth = difficulty()
        printboard(board)
        if player_count == 2:
            while not check4stuff(board, 0) and not full_board(board):
                color = 'R' if turn % 2 == 0 else 'B'
                print(f"{color}'s turn")
                placement = p_count(board)
                board[placement - 1].append(color)
                turn += 1
                printboard(board)
        else:
            while not check4stuff(board, 0) and not full_board(board):
                if turn % 2 == 0:
                    print('Your turn.\n')
                    placement = p_count(board)
                    board[placement - 1].append('R')
                else:
                    print('computer\'s turn...\n')
                    copy = deepcopy(board)
                    s = minimax(copy, depth)
                    print(str(s))
                    board[s].append('B')
                turn += 1
                printboard(board)
        if check4stuff(board, 0):
            winner = 'RED' if turn % 2 == 1 else 'BLACK'
            print(f'{winner} WINS')
        elif full_board(board):
            print('TIE GAME')

main_game()
