#-*- coding: cp1251-*-
# Задача 8 Вариант 7
# Доработайте	игру	"Анаграммы"	(см.	М.Доусон	Программируем	на	Python.	Гл.4) так,	чтобы	к	каждому	слову	полагалась	подсказка.	Игрок	должен	получать	право	на подсказку	в	том	случае,	если	у	него	нет	никаких	предположений.	Разработайте систему	начисления	очков,	по	которой	бы	игроки,	отгадавшие	слово	без	подсказки, получали	больше	тех,	кто	запросил	подсказку.
# Kochetkova I.A.
# 12.04.2017

import random
score=10
selection='нет'
name=''
list=('кошка','цветы','кружка','кровать','светильник')
word=random.choice(list)
answer=word
newword=''
while word:
    first=random.randrange(len(word))
    newword+=word[first]
    word=word[:first]+word[(first+1):]
print('Отгадайте анаграмму ',newword)
while name!=answer:
    name=input('\nВаш ответ: ')
    if name!=answer:
        print('\nВы ответили не правильно\n')
        selection=input('Хотите использовать подсказку? (да\нет)\n\n')
    if selection=='да':
        score-=5
        if answer=='кошка':
            print('Домашнее животное')
        elif answer=='цветы':
            print('Девушки любят, когда их дарят')
        elif answer=='кружка':
            print('Из нее пьют чай')
        elif answer=='кровать':
            print('Место сна')
        elif answer=='светильник':
            print('Источник света')
        selection='нет'
if name==answer:
    print('\nВы ответили правильно')
    score+=10
print('Итого у Вас',score,'очков')
input('\nНажмите ентер для выхода')
        
