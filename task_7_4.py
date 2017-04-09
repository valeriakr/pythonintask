#Задача №7, вариант № 4.

#1-50.	Разработайте	систему	начисления	очков	для	задачи	6,	в	соответствии	с	которой
#игрок	получал	бы	большее	количество	баллов	за	меньшее	количество	попыток.

#Довбыш Д.В.

import random

feats_numbers = random.randint(1,12)

if feats_numbers == 1 :
    feats = "Рождение и юность Геракла"
elif feats_numbers == 2 :
    feats = "Немейский лев"
elif feats_numbers == 3 :
    feats = "Лернейская гидра"
elif feats_numbers == 4 :
    feats = "Стимфалийские птицы"
elif feats_numbers == 5 :
    feats = "Керинейская лань"
elif feats_numbers == 6 :
    feats = "Критский бык"
elif feats_numbers == 7 :
    feats = "Кони Диомеда"
elif feats_numbers == 8 :
    feats = "Геракл у Адмета"
elif feats_numbers == 9 :
    feats = "Пояс Ипполиты"
elif feats_numbers == 10 :
    feats = "Коровы Гериона"
elif feats_numbers == 11 :
    feats = "Похищение Цербера"
elif feats_numbers == 12 :
    feats = "Золотые яблоки Гесперид"

trial = 11
bonus = 1000

while trial > 0 :
    answer = input("Назовите один из подвигов Геракла: ")
    if answer == feats :
        print("\nВы угадали!")
        print("Вам начислено", bonus, "баллов.")
        break
    else :
        print("\nВы не угадали!")
        if trial > 1 :
            print("Попробуйте еще раз.")
        else :
            print("Правильный ответ: ", feats)
        
    trial -= 1
    bonus -= 1000
	
input("\nНажмите Enter, чтобы выйти")
