# Задача 8. Вариант 16.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4)
# так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на
# подсказку в том случае, если у него нет никаких предположений. Разработайте
# систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки,
# получали больше тех, кто запросил подсказку.

# Смирнов Н.Н.
# 16.03.2017

import random


WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word
score_max = 120
hints = 1
final_score = 0
select_position_in_word = 1

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("""
    
    С Добро пожаловать в игру 'Анаграммы'!
    Надо переставить буквы так, чтобы получилось осмысленное слово.
    (Чтобы выйти из игры, введите "выйти, не вводя своей версии)
    """)

print("Вот анаграмма: ", jumble)

guess = input("\nПопробуйте отгадать исходное слово: \n")
while guess != correct:
    if guess.lower() == "выйти":
        score_max = 0
        break
    elif guess != correct and guess != "":
        print("K сожалению. вы неправы.")
        guess = input("Попробуйте отгадать исходное слово: \n")
    elif guess == "":
        print("Вы не ввели ни одного варианта.")
        request = input("Если вам нужна подсказка, введите 'подсказка'. \n")
        if request.lower() == "подсказка":
            hints += 1
            true_word = correct
            hint_word = true_word[:select_position_in_word]
            print("Слово начинается с ", hint_word)
            select_position_in_word += 1
            guess = input("Попробуйте отгадать исходное слово: \n")
    elif guess == correct:
        print("Дa, именно так! Вы отгадали!\n")

final_score = score_max // hints
print("Ваш счёт: " + str(final_score) + " очка(очков).")
print("Спасибо за игру! :)")


input("\n\nНажмите Enter, чтобы выйти.")