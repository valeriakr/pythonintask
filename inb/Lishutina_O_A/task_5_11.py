#Задача 5. Вариант 11.
#Напишите программу, которая бы при запуске случайным образом отображала имя одного из девяти оленей Санта Клауса.

#Lishutina O. A.
#17.03.2017

print("1 случайный олень Санто")

d = ['Dasher', 'Dancer', 'Prancer',
     'Vixen', 'Comet', 'Cupid',
     'Donder', 'Blitzen', 'Rudolph']

import random
print(random.choice(d))

input("\nНажмите Enter для выхода")