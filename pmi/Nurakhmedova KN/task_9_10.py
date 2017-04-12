#Нурахмедова Камиля Наилевна
#Вариант 10
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать,
#есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет".
#Вслед за тем игрок должен попробовать отгадать слово.
#Задача9

import random
WORDS = ("анаграмма", "питон", "игрок", "компьютер")
word=random.choice(WORDS)
number=len(word)
print('букв в слове: ' + str(number))

for i in range(5):
    k=0
    a=0
    number=len(word)
    check=word[a]
    letter=input('назовите букву: ')
    while (number >1):
         if (letter == check):
            k=k+1
            a=a+1
            check=word[a]
         else:
            a=a+1
            check=word[a]
         number=number - 1
    if (letter
        ==word[a]):
        k=k+1
    print ('Буква '+ '"'+ str(letter)+'"' + ' встречается в слове '+ str (k) + ' раз ')
answer=input ('Ваш ответ: ')

if (answer==word):
    print ('Поздравляем,вы выиграли! правильный ответ: ' + str(word))
else:
    print ('К сожалению вы проиграли.')
input ("\n\nНажмите ENTER для продолжения")
