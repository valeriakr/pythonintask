#-*- coding: cp1251-*-
# Задача 5 Вариант 7
# Напишите	программу,	которая	бы	при	запуске	случайным	образом	отображала имя	одного	из	семи	гномов,	друзей	Белоснежки
# Kochetkova I.A
# 04.04.2017
import random
print("Эта программа случайным образом выбирает одного из семи гномов Белоснежки")
otvet=random.randrange(7)+1
if otvet==1: 
  print("Проффесор")
elif otvet==2: 
  print("Ворчун")
elif otvet==3: 
  print("Весельчак")
elif otvet==4: 
  print("Скромник")
elif otvet==5: 
  print("Чихун")
elif otvet==6: 
  print("Соня")
elif otvet==7: 
  print("Молчун")
input("\n\nНажмите ентер")


