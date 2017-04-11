# Задача 8. Вариант 8.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
# Ermachenkov E. M.
# 28.03.2017
import random
score = 10
selection = 'нет'
name = ''
list = ('крот', 'собака', 'клавиатура', 'футболка', 'самолет')
word = random.choice(list)
answer = word
newword = ''
while word:
	first = random.randrange(len(word))
	newword += word[first]
	word = word[:first] + word[(first + 1):]
print('Попробуйте отгадать анаграмму ', newword)
while name != answer:
	name = input('\nВаш ответ: ')
	if name != answer:
		print('\nВы ответили не правильно\n')
		selection = input('Использовать подсказку? (да\нет)\n\n')
	if selection == 'да':
		score -= 5
		if answer == 'крот':
			print('Живет под землей')
		elif answer == 'собака':
			print('Не любит кошек')
		elif answer == 'клавиатура':
			print('Средство ввода')
		elif answer == 'футболка':
			print('Часть верхней одежды')
		elif answer == 'самолет':
			print('Воздушный вид транспорта')
		selection = 'нет'
if name == answer:
	print('\nВы ответили правильно')
	score += 10
print('У вас целых ', score, 'очков')
input('\nНажмите Enter для выхода')
