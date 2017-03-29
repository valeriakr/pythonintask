# Задача 7. Вариант 11.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой
# игрок получал бы большее количество баллов за меньшее количество попыток.

# Zaytsev N.S. 
# 04.03.2017

print ('Программа случайным образом загадывает название одного из девяти действующих вокзалов Москвы.')
print ('Вы должны угадать его.')
print ('\n\t\t\tП Р А В И Л А')
print ('\t\t=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
print ('Если вы угадываете - количество баллов утраивается.')
print ('Если ваш ответ неверен - отнимается количество баллов, равное номеру попытки.')
print ('\t\t=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
print ('\n\t\t\tНАЧИНАЕМ ИГРУ!')

import random #генерация случайных чисел
STATIONS = ['Белорусский', 'Казанский', 'Киевский', 'Курский', 'Ленинградский', 'Савёловский', 'Павелецкий', 'Рижский', 'Ярославский']
def menu():
	count = 1 #счетчик пунктов
	for station in STATIONS:
		print(str(count),')',station)
		count += 1
	print(count, ')','Сдаюсь')
def main():
	station = STATIONS[random.randint(0, len(STATIONS) - 1)]
	#счетчик попыток
	count = 1
	#начальное число очков игрока - случайная величина
	points = len(STATIONS) + random.randint(0,10)
	while True:
		print('У Вас', points, 'баллов.')
		if points <= 0:
			print('Увы, но вы проиграли!')
			print('Я загадал',station,'вокзал.')
			break
		menu() 
		answer = input('Выберете название вокзала (попытка № ' + str(count) + '): ')
		#введено неверное число из меню
		if int(answer) < 1 or int(answer) > len(STATIONS) + 1:
			continue
		#игрок сдался
		elif int(answer) == len(STATIONS) + 1:
			print('Я загадал',station,'вокзал.')
			break
		#игрок угадал
		elif STATIONS[int(answer) - 1] == station:
			#игрок угадал (утраиваем очки)
			points *= 3
			print('Вы выиграли!')
			print('У вас', points,'баллов.')
			break
		#игрок ошибся (продолжаем игру)
		else:
			print('Неверно!')
			#ответ неверный (отнимаем баллы, которые равны номеру попытки)
			points -= count
			STATIONS.remove(STATIONS[int(answer) - 1])
		count += 1
if __name__ == '__main__':
	main()
input ('\n\nPress ENTER to exit from program...')