# Задача 12. Вариант 13.
# Разработайте собственную стратегию ходов компьютера для игры "Крестики-нолики" (Задача 12).
# Перепишите функцию computer_move() в соответствии с этой стратегией..
# Salov A. S.
# 15.04.2017
X='X'
O='O'
EMPTY=' '
TIE='Ничья'
NUM_SQUARES=9
import random

def display_instruct():
	print(	"""
	Добро пожаловать в обитель логики и бессердечия.
	Здесь тебя ожидает жестокое интеллектуальное состязание!
	Чтобы сделать ход, введи число от 1 до 9 согласно полям доски:
					7 | 8 | 9
					---------
					4 | 5 | 6 
					---------
					1 | 2 | 3

	Да начнется битва!	В этот раз ходы у меня будут поразнообразней.			
			"""
	)

def ask_yes_no(question):
	response=None
	while response not in ('y', 'n'):
		response=input(question).lower()
	return response

def ask_number(question,low,high):
	response=None
	while response not in range(low, high+1):
		try:
			response=int(input(question))
		except ValueError:
			print('Ввидите номер позиции')
	return response

def pieces():
	pieces_choice=('y','n')
	go_first=random.choice(pieces_choice)
	if go_first=='y':
		print('\nВолею судеб первый ход за тобой, но это тебе не поможет! И да, ты играешь X')
		human=X
		computer=O
	else:
		print('\nБоюсь боги сегодня не на твоей стороне! Ты играешь "O"')
		computer=X
		human=O
	return computer, human

def new_board():
	board=[]
	for square in range(NUM_SQUARES+1):
		board.append(EMPTY)
	return board

def display_board(board):
	print("\n\t\t\t\t\t",board[7],"|",board[8],"|",board[9])
	print("\t\t\t\t\t","---------")
	print("\t\t\t\t\t",board[4],"|",board[5],"|",board[6])
	print("\t\t\t\t\t","---------")
	print("\t\t\t\t\t",board[1],"|",board[2],"|",board[3])

def legal_moves(board):
	moves=[]
	for square in range(NUM_SQUARES+1):
		if board[square]==EMPTY:
			moves.append(square)
	return moves

def winner(board):
	WAYS_TO_WIN= ((1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7),(1,4,7),(2,5,8),(3,6,9))
	for row in WAYS_TO_WIN:
		if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
			winner=board[row[0]]
			return winner
		if EMPTY not in board:
			return TIE
	return None

def human_move(board,human):
	legal=legal_moves(board)
	move=None
	while move not in legal:
		move=ask_number('Твой ход\n',1,NUM_SQUARES)
		if move not in legal:
			print('АХАХА, ты что, не видишь, что это место уже занято!?')
	print('хорошо...')
	return move
def choice_move():
	MOVES1=(5,1,3,7,9,2,4,6,8)
	MOVES2=(1,9,7,4,8,3,2,6,5)
	MOVES3=(3,7,1,4,2,5,8,9,6)
	MOVES4=(5,4,1,2,7,3,9,8,6)
	MOVES_CHOIСE=(MOVES1, MOVES2, MOVES3, MOVES4)
	return random.choice(MOVES_CHOIСE)
def computer_move(board,computer,human):
	board=board[:]
	BEST_MOVES=ALL_MOVES
	print('Я выбрал', end=' ')
	for move in legal_moves(board):
		board[move]=computer
		if winner(board)==computer:
			print(move)
			return move
		board[move]=EMPTY
	for move in legal_moves(board):
		board[move]=human
		if winner(board)==human:
			print(move)
			return move
		board[move]=EMPTY
	for move in BEST_MOVES:
		if move in legal_moves(board):
			print(move)
			return move

def next_turn(turn):
	if turn==X:
		return O
	else:
		return X

def congrat_winner(the_winner, computer, human):
	if the_winner!=TIE:
		print('Три', the_winner,'в ряд!\n')
	else:
		print('Силы оказались равны, ничья.')
	if the_winner==computer:
		print('ХА-Ха-ха-ха ну ничего, в слудеющий раз у тебя тоже не получится')
	elif the_winner==human:
		print('Хмм. Чудеса, видимо, случаются, но... этого просто не может быть!!!')

def main():
	global ALL_MOVES
	display_instruct()
	while True:
		ALL_MOVES=choice_move()
		computer, human=pieces()
		turn=X
		board=new_board()
		board[0]=None
		if computer==O:
			display_board(board)
		while not winner(board):
			if turn==human:
				move=human_move(board,human)
				board[move]=human
			else:
				move=computer_move(board,computer,human)
				board[move]=computer
			display_board(board)
			turn=next_turn(turn)
		the_winner=winner(board)
		congrat_winner(the_winner,computer,human)
		if ask_yes_no('Сыграем ещё? [y/n]\n')=='n':
			break
		else:
			continue

main()
input('Спасибо за игру, было не сложно, я смог.')