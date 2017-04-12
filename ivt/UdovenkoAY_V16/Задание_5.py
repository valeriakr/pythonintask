# Задача 5. Вариант 16.
# Напишите программу, которая бы при запуске случайным образом отображала имя одной из девяти муз в древнегреческой мифологии.
# Udovenko A. Y.
# 28.02.2017
import random
print (
    """
\a
\t\t\tДобро пожаловать в демонстрацию рандома и ветвления!
 Итак, вот одна из муз!
    """)
musa = random.randint(1, 9)
if musa == 1:
    print ("Каллиопа")
elif musa == 2:
    print ("Эвтерпа")
elif musa == 3:
    print ("Мельпомена")
elif musa == 4:
    print ("Талия")
elif musa == 5:
    print ("Эрато")
elif musa == 6:
    print ("Полигимния")
elif musa == 7:
    print ("Клио")
elif musa == 8:
    print ("Урания")
else:
    print ("Терпсихора")
input ("\n\tНажмите Enter, чтобы выйти")


