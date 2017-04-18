#	Задача	1.	Вариант	17
#	Создайте	игру,	в	которой	компьютер	загадывает	название	одного	из	пяти космических	челноков	проекта	Спейс	шаттл,	а	игрок	должен	его	угадать.
#	Tarasow	A.	V. #	01.04.2017
import random
from os import system,name
def cls(): system('cls' if name == 'nt' else 'clear')
def ochko(level):
	return 1500/level
print("\aНачнём Игру.\n Я загадываю один из шатлов 'Спейс Шаттла', а ты его отгадываешь.")
print("Вот их список:")
k="Колумбия"
c="Челленджер"
d="Дискавери"
a="Атлантис"
ee="Индевор"
print("\n",k,'\n',c,'\n',d,'\n',a,'\n',ee)
rand=random.randint(0,5)
if rand==0:
	otvet=k
	podskazka="Он мёртв"
elif rand==1:
	otvet=c
	podskazka="Одноимённый корабль исследовал океан в XIX веке"
elif rand==2:
	otvet=d
	podskazka="Он прослужил столько же лет, сколько нужно укланяться от армии"
elif rand==3:
	otvet=a
	podskazka="Брат Прометея"
elif rand==4:
	otvet=ee
	podskazka="Эдвин Хаббл благодарен этой штуке"
print("Кажется я загадал")
reshenie=1
n=1
while reshenie!=otvet:
	reshenie=input("Отвечай\n")

	ball=ochko(n)
	n+=1
	if reshenie!=otvet:

                print(podskazka)
                cls()
print("\n\nТы смог, но это было легко.",ball,"Твои баллы.")
input("\nНажмите Enter	для	выхода.")
