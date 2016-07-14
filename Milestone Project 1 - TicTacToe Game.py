board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
assign = {'x': 'Player 1 ', 'o': 'Player 2 '}


def game():
    player_move = True
    while True:
        print_board()
        while True:
            user_entry = raw_input("Please enter your move (row, column): ")
            move = valid_entry(user_entry,player_move)
            if not move:
                continue
            break
        player_move = not player_move
        board[move[1]-1][move[2]-1] = move[0]
        get = result()
        if not get:
            continue
        print_board()
        print get
        break


def valid_entry(user_entry,player_move):
    try:
        entry = user_entry.split(',')
        if len(entry) == 2:
            entry[0] = int(entry[0])
            entry[1] = int(entry[1])
            if isinstance(entry[0],int) and isinstance(entry[1],int):
                if entry[0] in [1,2,3] and entry[1] in [1,2,3]:
                    try:
                        if board[entry[0]-1][entry[1]-1] == ' ':
                            if player_move:
                                return ['x',entry[0],entry[1]]
                            else:
                                return ['o',entry[0],entry[1]]
                    except ValueError:
                        pass
                    print "Please enter index to a free block"
                    return False
    except ValueError:
        pass
    print "Please enter a valid index"
    return False

def result():
    for num in (0,1,2):
        if (len(set(board[num][:])) <= 1) and (board[num][0] != ' '):
            return assign[board[num][0]]+'wins'
        if len(set([x[num] for x in board])) <= 1 and (board[num][0] != ' '):
            return assign[board[0][num]]+'wins'
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != ' '):
        return assign[board[0][0]]+'wins'
    if (board[2][0] == board[1][1] == board[0][2]) and (board[2][0] != ' '):
        return assign[board[2][0]]+'wins'

    for line in board:
        for num in line:
            if num == ' ':
                return False
    return "Tie game"


def print_board():
    print board[0][:]
    print board[1][:]
    print board[2][:]

if __name__ == '__main__':
    game()