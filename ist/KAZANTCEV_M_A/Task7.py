# Задача 7. Вариант 13.

# Разработайте систему начисления очков для задачи 6, в соответствии с которой
# игрок получал бы большее количество баллов за меньшее количество попыток.

# Казанцев Максим.
# 03.03.2017

import random

print("Программа случайным образом загадывает один из спутников Марса, а игрок должен его угадать.")

satellite_numbers = random.randint(1, 3)

if satellite_numbers == 1:
    satellite = 'Фобос'
elif satellite_numbers == 2:
    satellite = 'Деймос'


trial = 3
bonus = 3000

while trial > 0:
    answer = input('\nНазовите один из спутников: ')
    if answer == satellite:
        print('\nВы угадали!')
        print('Вам начислено', bonus, 'баллов.')
        break
    else:
        print('\nВы не угадали!!!')
        if trial > 1:
            print('Попробуйте еще раз.')
        else:
            print('Правильный ответ: ', satellite)

    trial -= 1
    bonus -= 1000

input("\n\nНажмите Enter для выхода.")
