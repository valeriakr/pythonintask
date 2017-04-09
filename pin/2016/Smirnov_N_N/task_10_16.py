# Задача 10. Вариант 16.
# Напишите программу "Генератор персонажей" для игры. Пользователю должно
# быть предоставлено 30 пунктов, которые можно распределить между четырьмя
# характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
# пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
# туда из характеристик, которым он решил присвоить другие значения.

# Смирнов Н.Н.
# 18.03.2017

pool = 30
characteristics = {"Сила": "0", "Здоровье": "0", "Мудрость": "0", "Ловкость": "0"}

print("""
    Добро пожаловать в 'Генератор персонажей'.
    Вам дано 30 пунктов, которые необходимо распределить
    по 4 пунктам: Сила, Здоровье, Мудрость и Ловкость.
    """)
print("Текущее состояние: \n", characteristics, "\nДоступно для распределения: ", pool)

choice = ""
while True:
    print("""
    Введите 1 чтобы добавить пункты к любой характеристике.
    Введите 2 чтобы извлечь пункты из любой характеристики.
    Введите 3 чтобы просмотреть текущее распределение.
    Введите 4 чтобы выйти.
    """)
    choice = input()
    if choice == "":
        print("Пожалуйста, введите номер пункта перед тем как нажать на Enter!")
    elif int(choice) == 1:
        if pool > 0:
            print("Вы решили добавить пункты к любой характеристике. \n")
            name_of_the_characteristic = input("Введите название характеристики: \n")
            if name_of_the_characteristic.title() in characteristics:
                restore = int(characteristics[name_of_the_characteristic.title()])
                quantity_of_the_characteristic = int(input("Введите количество, которое необходимо добавить к характеристике: \n"))
                сheck_for_a_negative_value = pool - quantity_of_the_characteristic
                if restore <=30 and сheck_for_a_negative_value >= 0:
                    restore += quantity_of_the_characteristic
                    characteristics[name_of_the_characteristic.title()] = restore
                    pool -= quantity_of_the_characteristic
                    print(quantity_of_the_characteristic, " пункта(пунктов) добавлено(добавлены) к ", name_of_the_characteristic.title())
                    print("У вас осталось ", pool, " пункта(пунктов) доступных для распределения.")
                else:
                    print("Вы не можете присвоить характеристике значение больше доступного. \n"
                          "Измените количество, которое необходимо добавить к характеристике.")
            else:
                print("Данная характеристика не предоставлена к изменениям. Повторите попытку.")
        else:
            print("У вас закончились очки(пункты) для распределения по характеристикам. \n"
                "Вы больше не можете ничего добавить.\n"
                "Однако, вы можете воспользоваться пунктом 2 в меню и извлечь их из любой другой характеристики.")
    elif int(choice) == 2:
        print("Вы решили извлечь пункты от любой из характеристик. \n")
        name_of_the_characteristic = input("Введите название характеристики: \n")
        if name_of_the_characteristic.title() in characteristics:
            restore = int(characteristics[name_of_the_characteristic.title()])
            if restore > 0:
                quantity_of_the_characteristic = int(input("Введите количество, которое необходимо вернуть из характеристики: \n"))
                restore -= quantity_of_the_characteristic
                if restore >= 0:
                    characteristics[name_of_the_characteristic.title()] = restore
                    pool += quantity_of_the_characteristic
                    print(quantity_of_the_characteristic, " пункта(пунктов) возвращены от ", name_of_the_characteristic.title())
                    print("У вас стало ", pool, " пункта(пунктов) доступных для распределения.")
                else:
                    print("Вы не можете присвоить характеристике отрицательное значение. \n"
                          "Измените количество, которое необходимо вернуть из характеристики.")
            else:
                print("Этой характеристике ещё не было присвоино ни одного пункта(зачения).")
        else:
            print("Данная характеристика не предоставлена к изменениям. Повторите попытку.")
    elif int(choice) == 3:
        print("Вы решили просмотреть текущее распределение. \n")
        print("Вы имеете: \n", characteristics)
        print("Доступно для распределения: ", pool)
    elif int(choice) == 4:
        print("Вы воспользовались выходом.")
        break
    else:
        print("Данного пункта в меню нет. Будьте внимательнее.")

print("Генератор персонажей закончил свою работу.")


input("\n\nНажмите Enter, чтобы выйти.")