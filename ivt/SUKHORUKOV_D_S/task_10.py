# Задача 10.
#  Напишите программу "Генератор персонажей" для игры. Пользователю должно
# быть предоставлено 30 пунктов, которые можно распределить между четырьмя
# характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
# пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
# туда из характеристик, которым он решил присвоить другие значения.

# Сухоруков Д. С.

# 15.04.17

intro           = '\t\tДобро пожаловать в программу "Генератор персонажей"'
msgGetFirst     = '\n\tВам предоставлено %d пунктов, которые можно распределить между четырьмя характеристиками.'
msgGet          = '\n\tУ Вас осталось пунктов: %d. '
msgAddAnother   = 'Добавить характеристику'
msgEnterMenu    = 'Выберите характеристику: '
msgEnter        = 'Введите значение: '
msgAddNewName   = 'Введите название: '
msgAddHeroName  = '\n\tВведите имя персонажа: '
msgErrValue     = 'Ошибка! Некоректное значение!'
final           = '\n\t%s имеет следующие характеристики:'
points          = 30
heroName        = ''
characteristics = [["Сила",0],["Здоровье",0],["Мудрость",0],["Ловкость",0]]
isFirst         = True

def getChars():
        i = 0 
        while i < len(characteristics):
                        print('\t%d - %s\t= %d' % (i,characteristics[i][0],characteristics[i][1]))
                        i += 1
        return i # номер для новой характеристики

print(intro)
while points > 0:
        newValue = 0
        if isFirst: # первый ввод
                print(msgGetFirst % points)
                heroName = input(msgAddHeroName)
                isFirst = False
        else:
                print(msgGet % points)
        print('\t%d - %s\t' % (getChars(),msgAddAnother))
        selected = input(msgEnterMenu)
        if (not selected.isnumeric()):
                print(msgErrValue)
        elif (int(selected) == len(characteristics)): # выбрано добавление
                newName  = input(msgAddNewName)
                newValue = int(input(msgEnter))
                characteristics.append([newName,newValue])
        elif (int(selected) <= len(characteristics) and (int(selected) >= 0)): # входит
                newValue = int(input(msgEnter))
                characteristics[int(selected)][1] += newValue
        else:
                print(msgErrValue)
        points -= int(newValue)
        
print(final % heroName)
getChars()
input('Для выхода нажмите Enter')


