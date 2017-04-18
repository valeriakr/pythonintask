# Задача 9. Вариант 5
# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.+

#Bobykina D.A.
# 16.04.2017
# Объяснение условий игроку.
print("Вам предоставлено 30 пунктов,которые нужно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловколсть")
 
sila = 0
zdorovie = 0
mudrost = 0
lovkost = 0
choice = None
global_choice = None
 
while global_choice != 0:
 
    
    ost_points = (30 - sila - zdorovie - mudrost - lovkost)
    print("Таблица характеристик на данный момент: \n"
        "\t\t\t1. Сила:", sila, "\n"
        "\t\t\t2. Здоровье:",zdorovie, "\n"
        "\t\t\t3. Мудрость:", mudrost, "\n"
        "\t\t\t4. Ловкость:", lovkost, "\n\n"
        "\t\t\tУ вас осталось пунктов:", ost_points, "\n" )
 
    print("Что вы хотите сделать сейчас?\n"
        "\t\t\t1. Добавить пункты в одну из характеристик.\n"
        "\t\t\t2. Убрать пункты из характеристики.\n"
        "\t\t\t3. Закончить распределиние пунктов.\n")
    global_choice = int(input())
    if global_choice == 1:
        print("В какую из характеристик вы хотите добавить пункты?\n"
            "\t\t\t1. Сила.\n"
            "\t\t\t2. Здоровье.\n"
            "\t\t\t3. Мудрость.\n"
            "\t\t\t4. Ловкость.\n")
        choice = int(input())
        if choice == 1:
            print("Сколько пунктов вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                strength += scores
            else:
                print("Невозможно добавить пункты.\n")
        elif choice == 2:
            print("Сколько пунктов вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                health += scores
            else:
                print("Невозможно добавить пункты.\n")
        elif choice == 3:
            print("Сколько пунктов вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                wisdom += scores
            else:
                print("Невозможно добавить пункты.\n")
        elif choice == 4:
            print("Сколько пунктов вы хотите добавить?\n")
            scores = int(input())
            if scores >= 0 and scores <= ost_points:
                agility += scores
            else:
                print("Невозможно добавить пункты.\n")
 
    elif global_choice == 2:
        print("Из какой характеристики вы хотите убрать очки?\n"
            "\t\t\t1. Сила.\n"
            "\t\t\t2. Здоровье.\n"
            "\t\t\t3. Мудрость.\n"
            "\t\t\t4. Ловкость.\n")
        choice = int(input())
        if choice == 1:
            print("Сколько пунктов вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (strength - scores) >= 0:
                strength -= scores
            else:
                print ("Невозможно добавить пункты. \n")
        elif choice == 2:
            print("Сколько пунктов вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (health - scores) >= 0:
                health -= scores
            else:
                print("Невозможно добавить пункты.\n")
        elif choice == 3:
            print("Сколько пунктов вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (wisdom - scores) >= 0:
                wisdom -= scores
            else:
                print("Неввозможно добавить пункты.\n")
        elif choice == 4:
            print("Сколько пунктов вы хотите убрать?\n")
            scores = int(input())
            if scores >= 0 and (agility - scores) >= 0:
                agility -= scores
            else:
                print("Невозможно добавить пункты.\n")
 
    
    elif global_choice == 3:
        if ost_points == 0:
            break
        else:
            print("Используйте все очки, данные вам!\n")
 
 
print("Ваш герой готов! Таблица его характеристик выглядит так: \n"
    "\t\t\t1. Сила:", strength, "\n"
    "\t\t\t2. Здоровье:", health, "\n"
    "\t\t\t3. Мудрость:", wisdom, "\n"
    "\t\t\t4. Ловкость:", agility, "\n")
 
input("\nНажмите Enter, чтобы выйти")
