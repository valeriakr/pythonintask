#-*- coding: cp1251-*-
# Задача 9 Вариант 7
# Создайте	игру,в которой компьютер выбирает какое-либо слово,	а	игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять	попыток узнать,	есть ли	какая-либо	буква в	слове, причем программа	может отвечать	только "Да"	или "Нет".	Вслед	за	тем	игрок	должен	попробовать	отгадать	слово.
# Kochetkova I.A.
# 12.04.2017

import random
words=('университет','тетрадь','ручка','аудитория')
word=random.choice(words)
number=len(word)
print('Я загадал слово, ваша задача его отгадать.')
print('Количесво букв в слове: '+str(number))
for i in range(5):
    k=0
    a=0
    number=len(word)
    check=word[a]
    letter=input('Напишите букву: ')
    while (number>1):
        if (letter==check):
            k=k+1
            a=a+1
            check=word[a]
        else:
            a=a+1
            check=word[a]
        number=number-1
    if (letter==word[a]):
        k=k+1
    print('Буква '+'"'+str(letter)+'"'+' встречается в слове '+str(k)+' раз')
answer=input('\n\nВаш ответ: ')
if (answer==word):
    print('Вы выиграли! это правильнй ответ: '+str(word))
else:
    print('Жаль, выиграть Вам не удалось')
input('\nНажмите ентер для выхода')