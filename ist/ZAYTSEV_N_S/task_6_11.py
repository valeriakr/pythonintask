# Задача 6. Вариант 11.
# Создайте игру, в которой компьютер загадывает название одного из девяти
# действующих вокзалов Москвы, а игрок должен его угадать.

# Zaytsev N.S. 
# 04.03.2017

print ('Программа случайным образом загадывает название одного из девяти действующих вокзалов Москвы.')
print ('Игрок должен его угадать.')
print ('\n')

import random #генерация случайных чисел
STATIONS = ['Белорусский', 'Казанский', 'Киевский', 'Курский', 'Ленинградский', 'Савёловский', 'Павелецкий', 'Рижский', 'Ярославский']
def menu():
	count = 1
	for station in STATIONS:
		print(str(count),')', station)
		count += 1
	print(count, ')','Cдаюсь')
def main():
	#случайным образом выбрать 1 из 9 вокзалов
	station = STATIONS[random.randint(0, len(STATIONS) - 1)]
	count = 1
	while True:
		#попросить игрока выбрать название вокзала
		menu() #вывести меню выбора вокзала
		answer = input('Выберете название вокзала (попытка № ' + str(count) + '): ')
		#введено неверное число для пункта (игнорируем)
		if int(answer) < 1 or int(answer) > len(STATIONS) + 1:
			continue
		#игрок сдался
		elif int(answer) == len(STATIONS) + 1:
			print('Я загадал', station,'вокзал')
			break
		#название угадано
		elif STATIONS[int(answer) - 1] == station:
			print('Вы выиграли!')
			break
		#игрок ошибся, продолжаем игру
		else:
			print('Неверно!')
			#удаляем из списка названный вокзал
			STATIONS.remove(STATIONS[int(answer) - 1])
		count += 1
if __name__ == '__main__':
	main()
input ('\n\n\nPress ENTER to exit from program...')