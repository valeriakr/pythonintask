#Задача 5. Вариант 6
#Напишите программу, которая бы при запуске случайным образом отображала
#название одного из двух спутников Марса.

#Bogdanova A. V.

import random
print("У планеты Марс есть два спутника.")
print("Сейчас я назову вам один из них: ")
sputnik=random.randint(1,2)
if sputnik==1:
    print( \
    """
        Фобос
              """)
elif sputnik==2:
      print( \
      """
         Деймос
              """)
input("\nPress the enter key to exit.")
