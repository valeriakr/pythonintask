# Задача 5. Вариант 11.
# Напишите программу, которая бы при запуске случайным образом отображала
# имя одного из девяти оленей Санта Клауса.

# Zaytsev N.S. 
# 18.02.2017

print ("Данная программа случайным образом отображает имя одного из девяти оленей Санта Клауса")
import random
import string
# создаем список имён оленей
deer = ["Dasher","Dancer","Prancer","Vixen","Comet","Cupid","Donder","Blitzen","Rudolf"]
print("\nОдного из оленей Санта Клауса звали ", random.choice(deer))
input("\n\n\n\n\n\nPress Enter to exit from program...")
