# Pyatkin Pavel Yur`evich
# Variant 11

import random
RailwayStation = [ 'Белорусский', 'Казанский', 'Киевский', 'Курский', 'Ленинградский', 'Павелецкий', 'Рижский', 'Савёловский', 'Ярославский']
VvodRailwayStation=input ('Назовите один из Московских вокзалов:')
a=random.choice(RailwayStation)
if a==RailwayStation:
print ('Вы угадали! \n Правильный ответ',a)
else:
print('Вы не угадали ! \n Правильный ответ', a)
input ('Нажмите Enter')