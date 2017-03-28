# Задача 5. Вариант 10.
# Напишите программу, которая бы при запуске случайным образом отображала название одного из шести континентов Земли.

# Lisyanskaya A.V.
# 14.03.2017

import random
kontin1 = ("Азия")
kontin2 = ("Африка")
kontin3 = ("Америка")
kontin4 = ("Австралия")
kontin5 = ("Антарктида")
kontin6 = ("Европа")
vibor = random.randint(1, 6)
if vibor == 1:
    print(kontin1)
elif vibor == 2:
    print(kontin2)
elif vibor == 3:
    print(kontin3)
elif vibor == 4:
    print(kontin4)
elif vibor == 5:
    print(kontin5)
else:
    print(kontin6)
input("\n\nНажмите Enter, чтобы выйти.")
