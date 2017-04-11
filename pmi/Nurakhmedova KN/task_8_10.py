#Нурахмедова Камиля Наилевна
#Вариант 10
#Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка.
#Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
#Разработайте систему начисления очков, по которой бы игроки,
#отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
#Задача 8.
import random
WORDS=("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word=random.choice(WORDS)
correct=word
jumble=""
finish=len(word)
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]
print("Добро пожаловать в игру 'Анаграммы'!",
      "\nНадо пререставить буквы так, чтобы получилось осмысленное слово.",
      "\n(Для выхода нажмите Enter, не вводя своей версии)")
print("Вот анаграмма: ", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")
y=100
x= ""
while y>0:
	if guess.lower() == correct:
		print("Да, именно так! Вы отгадали!\n")
		break
	else:
		print("К сожалению, вы неправы!")
		for letter in correct:
			x += letter
			if guess == correct:
				break
			print("Подсказка: ", x)
			y=y-1
			if y==0:
				break
			start = 0
			if x == correct[start:finish]:
				break
			guess = input("Попробуйте отгадать исходное слово: ")
		if guess != correct:
			y=0
		break
print("Количество очков: ", y)
print("Спасибо за игру!")
input("\n\nНажмите Enter, чтобы выйти.")
