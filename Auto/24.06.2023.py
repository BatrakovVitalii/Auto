# В игре компьютер создает один одноклеточный корабль на поле 5 на 5. У нас есть ограниченное число попыток по нему попасть. У нас нет поля - тут мы только нападаем.
import random
# Создание заготовки для поля - списка из 5 списков по 5 элементов
board = []
for x in range(5):
    board.append(['0'] * 5)

# Создание поля
def print_board(board):
    for row in board:
        print((''.join(row))) # соединяет список в строку

print('Sea Battle')
print_board(board)

# Тела функций для задания координат корабля
def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)


ship_row = random_row(board) # Одновременно вызов функции и присвоение результата ее работы переменной (задали координату корабля по горизонтали)
ship_col = random_col(board) # Одновременно вызов функции и присвоение результата ее работы переменной (задали координату корабля по вертикали)

# Основной цикл игры

for turn in range(4): # кол-во попыток, задается произвольно, не больше размера поля
    print('Ход', turn + 1)
    guess_row = int(input('(0-4): ')) # Задаем координату выстрела по горизонтали
    guess_col = int(input('(0-4): ')) # Задаем координату выстрела по вертикали

# Проверка попадания

    if guess_row == ship_row and guess_col == ship_col:
        print('Victory!')
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print('Допустимы значения (0-4)..')
        elif board[guess_row][guess_col] == 'X': # Это элемент с двумя индексами списка
            print('Уже стреляли')
        else:
            print('Мимо')
            board[guess_row][guess_col] = 'X' # Это элемент с двумя индексами списка
            if turn == 3:
                print('Конец игры')
            print_board(board)

