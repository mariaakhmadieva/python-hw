# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))
win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
    print('-------------')

def take_input(player_token):
    while True:
        val = input('Куда поставить ' + player_token + '? ')
        if not (val in '123456789'):
            print('Введены некорректные данные, попробуйте заново.')
            continue
        val = int(val)
        if str(board[val - 1]) in 'X0':
            print('Клетка занята.')
            continue
        board[val - 1] = player_token
        break

def check_win():
    for i in win_coord:
        if (board[i[0]]) == (board[i[1]]) == (board[i[2]]):
            return board[i[0]]
    else:
        return False

def main():
    count = 0
    while True:
        draw_board()
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('0')
        if count > 3:
            winner = check_win()
            if winner:
                draw_board()
                print('✨Выиграл', winner + '!✨')
                break
        count += 1
        if count > 8:
            draw_board()
            print('Ничья! 😎')
            break

main()