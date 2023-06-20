import random


def is_borders(left_border, right_border):             # Проверка границ
    if left_border <= right_border:
        return True
    else:
        return False


def is_valid(number, left_border, right_border):               # Проверка на нахождение числа в границах
    if left_border <= number <= right_border:
        return True
    else:
        return False


def game_choose_number():
    while True:
        print("Введите две границы через пробел для игры: ", end="")
        left_border, right_border = map(int, input().split())           #Ввод границ
        if is_borders(left_border, right_border):             # Проверка границ
            riddle = random.randint(left_border, right_border)
            print(f"Число загадано в диапазоне от {left_border} до {right_border} включительно!")
            print("Ваше число: ", end="")
            count_for_3_false = 0
            count_tries = 0
            while True:
                hypothesis = int(input())
                if is_valid(hypothesis, left_border, right_border):         # Проверка на нахождение числа в границах
                    count_tries += 1
                    count_for_3_false= 0
                    if hypothesis > riddle:
                        print(f"{hypothesis} - слишком много, попробуйте еще раз: ", end="\n")
                    elif hypothesis < riddle:
                        print(f"{hypothesis} - слишком мало, попробуйте еще раз: ", end="\n")
                    else:
                        print("Вы угадали, поздравлфяем!")
                        print(f"Вы справились за {count_tries} попыток. Неплохо!")
                        break
                else:
                    count_for_3_false += 1
                    if count_for_3_false == 3:
                        print(f"А может быть все-таки введем целое число от {left_border} до {right_border}?")
                    else:
                        print("Вы ввели некорректное число!")
                        print("Попробуйте еще раз: ", end="")
            print()
            print('Спасибо, что играли в числовую угадайку!')
            print("Если вы хотите выйти из игры, то введите 'exit'")
            print("Но если вы хотите сыграть еще раз, то введите 'play'")
            while True:
                answer = input()
                if answer == "play":
                    print("Ага! Ну, тогда поехали!")
                    game_choose_number()
                elif answer == "exit":
                    return print("До свидания!")
                    pass
                else:
                    print("Игра вас не поняла. Повторите, пожалуйста.")
        else:
            print("Что-то не так с границами! Поправьте их!")
            print()


game_choose_number()