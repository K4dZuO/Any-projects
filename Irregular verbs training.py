import csv
import random
import sys


def get_info():
    with open("irregular.csv") as file:
        reader = csv.reader(file)
        mass = []
        for x in reader:
            row = x[0].split(";")
            mass.append(row)
        mass = mass[1:]
        #print(mass)
    return mass


def end(wrong_answers):
    print()
    print("-"*100)
    print()
    i = 1
    print("Глаголы, в которых ты совершил ошибки:")
    for row in wrong_answers:
        print(i, *row.split())
        i += 1
    print()
    return "Пока! Приходи тренироваться еще!"


def round(rus_verbs, mass, count, wrong_answers):
    if len(rus_verbs) == 0:
        print(end(wrong_answers))
        sys.exit()
    rus_verb = random.choice(rus_verbs)
    print(f"Глагол '{rus_verb}'")
    user_answer = " ".join(input("Ваш ответ:        ").split())
    if user_answer == "end":
        print(end(wrong_answers))
        sys.exit()
    else:
        for row in mass:
            if row[0] == rus_verb:
                index = mass.index(row)
                row_answer = mass[index]
                program_answer = " ".join(row_answer[1:])
        print(f"Правильный ответ: {program_answer}")
        if user_answer == program_answer:
            print("Правильно!")
            count += 1
        else:
            print("Неправильно!")
            program_answer = rus_verb + " " + program_answer
            wrong_answers.append(program_answer)
        mass.pop(index)
        rus_verbs.pop(index)
        print(f"В списке осталось {len(mass)} глаголов.")
        return count, wrong_answers, mass


def main():
    print("Учи, учи давай, учи!")
    print("Каждый ответ должен выглядеть как 'go went gone'. Иначе не робит(")
    print("За каждый правильный ответ ты получаешь 1 балл.")
    print("Если хочешь закончить и посмотреть глаголы, в которых ты ошибся, то в поле ответа введи 'end'.")
    print("Помни, всего в списке 112 глаголов.")
    print("Начнем же тренировку!")
    print()
    mass = get_info()
    rus_verbs = [row[0] for row in mass]
    count = 0
    wrong_answers = []
    while True:
        count, wrong_answers, mass = round(rus_verbs, mass, count, wrong_answers)
        print()
        print(f"Сейчас у вас {count} баллов")
        print()
main()


