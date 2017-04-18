# Задача 10. Вариант 11.
# Напишите программу "Генератор персонажей" для игры.
# Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками:
# Сила, Здоровье, Мудрость и Ловкость.
# Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула",
# но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

# Лишутина О. А.
# 11.04.2017

print(
"""
			Добро пожаловать в 'Генератор персонажей'!
	Здесь Вы можете создать своих персонажей со своими характеристиками.
		Всего на каждого персонажа отводится 30 пунктов.
Пункты могут быть распределены между: Силой, Здоровьем, Мудростью, Ловкостью.
"""
)
personagi = {'Виктория': ['Виктория', 0, 0, 0, 0]}
vibor = None
while vibor != 0:
	print(
	"""
	Нажмите 1, чтобы добавить персонажа
	Нажмите 2, чтобы редактировать персонажа
	Нажмите 3, чтобы просмотреть имеющихся персонажей
	Нажмите 4, чтобы удалить персонажа
	"""
		)
	vibor = int(input("Что вы хотите сделать: "))
	if vibor == 1:
		name = input("Как Вы назовете нового персонажа: ")
		n = name
		if name not in personagi:
			personagi[name] = [n, "sila", "zdorovie", "mudrost", "lovkost"]
			punkti = 30
			personagi[name][0] = name
			s = int(input("\nЗначение Силы: "))
			while s < 0 or s > 30:
				s = int(input("Такого значения не существует. Введите правильное значение:"))
			personagi[name][1] = s
			punkti = punkti - s
			z = int(input("\nЗначение Здоровья: "))
			while z < 0 or z > punkti:
				z = int(input("Такого значения не существует. Введите правильное значение:"))
			personagi[name][2] = z
			punkti = punkti - z
			m = int(input("\nЗначение Мудрости: "))
			while m < 0 or m > punkti:
				m = int(input("Такого значения не существует. Введите правильное значение:"))
			personagi[name][3] = m
			punkti = punkti - m
			l = int(input("\nЗначение Ловкости: "))
			while l < 0 or l > punkti:
				l = int(input("Такого значения не существует. Введите правильное значение:"))
			personagi[name][4] = l
			punkti = punkti - l
			print("Персонаж добавлен.")
		else:
			print("Такое имя уже существует.")
	elif vibor == 2:
		name = input("Введите имя персонажа: ")
		n = name
		if name in personagi:
			personagi[name] = [n, "sila", "zdorovie", "mudrost", "lovkost"]
			punkti = 30
			personagi[name][0] = name
			s = int(input("\nЗначение Силы: "))
			while s < 0 or s > 30:
				s = int(input("Такого значения не существует. Введите правильное значение:"))
			personagi[name][1] = s
			punkti = punkti - s
			z = int(input("\nЗначение Здоровья: "))
			while z < 0 or z > punkti:
				z = int(input("Такого значения не существует. Введите правильное значение:"))
			personagi[name][2] = z
			punkti = punkti - z
			m = int(input("\nЗначение Мудрости: "))
			while m < 0 or m > punkti:
				m = int(input("Такого значения не существует. Введите правильное значение:"))
			personagi[name][3] = m
			punkti = punkti - m
			l = int(input("\nЗначение Ловкости: "))
			while l < 0 or l > punkti:
				l = int(input("Такого значения не существует. Введите правильное значение:"))
			personagi[name][4] = l
			punkti = punkti - l
			print("Персонаж", name, "изменен.")
		else:
			print("Такого персонажа не существует.")
	elif vibor == 3:
		print("Ваши персонажи:")
		for name in personagi:
			print(name)
	elif vibor == 4:
		name = input("Какого персонажа Вы хотите удалить? ")
		if name in personagi:
			del personagi[name]
			print("Персонаж удален.")
		else:
			print("Такого персонажа не существует.")
	else:
		print ("Такого пункта не существует.")
input("\n\nНажмите Enter, чтобы выйти.")