# Задача 6. Вариант 9.

#Создайте игру, в которой компьютер загадывает имя одного из трех поросят, а игрок должен его угадать.

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

answer = input('\nНазовите одного из поросят: ')

if answer == animal :
    print('\nВы угадали!')
else :
    print('\nВы не угадали!!!')
    print('Правильный ответ: ', animal)

input("\n\nНажмите Enter для выхода.")
