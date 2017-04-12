# Задача 6. Вариант 9.

#Разработайте систему начисления очков для задачи 6, в соответствии с которой 
#игрок получал бы большее количество баллов за меньшее количество попыток.

# Lungu R.U.
# 11.04.2017

import random

print("Программа случайным образом загадывает название одного из 3-х поросят, а игрок должен его угадать.")

animal_numbers = random.randint(1,3)

if animal_numbers == 1 :
    animal = 'Ниф-Ниф'
elif animal_numbers == 2 :
    animal = 'Наф-Наф'
elif animal_numbers == 3 :
    animal = 'Нуф-Нуф' 

trial = 3
bonus = 3000

while trial > 0 :
    answer = input('\nНазовите одного из поросят: ')
    if answer == animal :
        print('\nВы угадали!')
        print('Вам начислено', bonus, 'баллов.')
        break
    else :
        print('\nВы не угадали!!!')
        if trial > 1 :
            print('Попробуйте еще раз.')
        else :
            print('Правильный ответ: ', animal)
        
    trial -= 1
    bonus -= 1000

		
input("\n\nНажмите Enter для выхода.")
