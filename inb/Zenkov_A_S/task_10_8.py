# Задача 10. Вариант 8.
# Напишите программу "Генератор персонажей" для игры. 
# Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: 
# Сила, Здоровье, Мудрость и Ловкость. 
# Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", 
# но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

# Zenkov A. S.
# 11.04.2017

print("Добро пожаловать в Генератор персонажей.\nСоздайте персонажа,распределив характеристики.\nНа одного персонажа отводится 30 пунктов.\nРаспределите пункты между параметрами:\n  1)Сила\n  2)Здоровье\n  3)Мудрость\n  4)Ловкость")
characters = {'Грогнак': ['Грогнак', 0, 0, 0, 0]}
choice = None
while choice != 0:
	print("Управление:\n*1* - добавить персонажа\n*2* - редактировать персонажа\n*3* - просмотреть список персонажей\n*4* - удалить персонажа")
	choice = int(input("Что вы хотите сделать?"))
	if choice == 1:
		name = input("Имя нового персонажа: ")
		n = name
		if name not in characters:
			characters[name] = [n, "sila", "zdorovie", "mudrost", "lovkost"]
			points = 30
			characters[name][0] = name
			s = int(input("\nЗначение Силы: "))
			while s < 0 or s > points:
				s = int(input("Введите значение от 0 до 30: "))
			characters[name][1] = s
			points = points - s
			z = int(input("Значение Здоровья: "))
			while z < 0 or z > points:
				z = int(input("Введите значение от 0 до 30: "))
			characters[name][2] = z
			points = points - z
			m = int(input("Значение Мудрости: "))
			while m < 0 or m > points:
				m = int(input("Введите значение от 0 до 30: "))
			characters[name][3] = m
			points = points - m
			l = int(input("Значение Ловкости: "))
			while l < 0 or l > points:
				l = int(input("Введите значение от 0 до 30: "))
			characters[name][4] = l
			points = points - l
			print("\t***Персонаж успешно добавлен.***\n")
		else:
			print("\tТакое имя уже используется.")
	elif choice == 2:
		name = input("\nВведите имя персонажа: ")
		n = name
		if name in characters:
			characters[name] = [n, "sila", "zdorovie", "mudrost", "lovkost"]
			points = 30
			characters[name][0] = name
			s = int(input("\nЗначение Силы: "))
			while s < 0 or s > points:
				s = int(input("Введите значение от 0 до 30: "))
			characters[name][1] = s
			points = points - s
			z = int(input("Значение Здоровья: "))
			while z < 0 or z > points:
				z = int(input("Введите значение от 0 до 30: "))
			characters[name][2] = z
			points = points - z
			m = int(input("Значение Мудрости: "))
			while m < 0 or m > points:
				m = int(input("Введите значение от 0 до 30: "))
			characters[name][3] = m
			points = points - m
			l = int(input("Значение Ловкости: "))
			while l < 0 or l > points:
				l = int(input("Введите значение от 0 до 30: "))
			characters[name][4] = l
			points = points - l
			print("\t***Персонаж", name, "изменен.***\n")
		else:
			print("\tТакого персонажа не существует.")
	elif choice == 3:
		print("Список созданных персонажей:")
		for name in characters:
			print(name, '\n')
	elif choice == 4:
		name = input("\nКакого персонажа удалить? ")
		if name in characters:
			del characters[name]
			print("***Персонаж удален.***")
		else:
			print("\tТакого персонажа не существует.")
	else:
		print ("Такого пункта не существует.")
input("\n\nНажмите Enter, чтобы выйти.")
