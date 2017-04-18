#Лаб №11 вариант 2
#Игра крестики нолики
#Выполнила Алхасова Разият ИНБ-2016-1

X = 'X'
O = 'O'
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9


def display_instruct():
    """Инструкция"""
    print(
    """
    Добро пожаловать в игру 'Крестики нолики'
    Вам чтобы сделать ход нужно ввести число от 0 до 8.
    Числа соответствуют полям доски - так, как показано ниже:
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    """
    )


def ask_yes_no(question):
    """Вопрос Да Нет"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Введите число"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определяет первый ход"""
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? (y/n): ")
    if go_first == 'y':
        print("\nХорошо, ходи крестиками")
        human = X
        computer = O
    else:
        print("\nХорошо, играй ноликами")
        human = O
        computer = X
    return computer, human


def new_board():
    """Создает новую игровую доску"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает игровую доску"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Создет список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """определяет победителя в игре"""
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    """Ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход, выбери одно из полей (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭто поле уже занято, выбери другое\n")
    print("Ладно...")
    return move


def computer_move(board, computer, human):
    """Компьютерный ход"""
    board = board[:]
    BEST_MOVES = (5, 2, 1, 8, 0, 4, 6, 3, 7)
    print("Я выбираю поле №", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Переход хода"""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Поздравление"""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд\n")
    else:
        print("Ничья\n")
    if the_winner == computer:
        print("Все таки компьютер умнее человека\n")
    elif the_winner == human:
        print("Тебе просто повезло\n")
    elif the_winner == TIE:
        print("Ничья")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

main()
input("\n\nНажмите Enter чтобы выйти")