import random

def replay():
    print()
    print()
    print("Хотите сыграть еще раз? Напишите '1', если да, и '0', если хотите выйти.")
    result = int(input())
    return result


def choose_the_letter(word_answer):
    print("""    _______________
    |                     
    |             
    |             
    |            
    |             
    |                      
    |
    |    """)
    print()
    answer = word_answer
    word_answer = list(answer)
    dictinonary = list()
    print("Слово загадано!")
    word_mistery = list("*" * len(word_answer))
    print("".join(word_mistery))
    #print(answer, word_answer, word_mistery)
    count_of_mistakes = 0
    while "*" in word_mistery and count_of_mistakes != 6:
        print("Введите букву: ", end="")
        letter = input()
        if letter in dictinonary :
            print("Вы уже использовали эту букву!")
        else:
            dictinonary.append(letter)
            if letter in word_answer:
                print(f"Верно! Откройте букву {letter}!")
                while letter in word_answer:
                    index = word_answer.index(letter)
                    word_mistery[index] = letter
                    word_answer[index] = "*"
                print("".join(word_mistery))
                print()
                print()
            else:
                print("Такой буквы в слове нет!")
                count_of_mistakes += 1
                if count_of_mistakes == 1:
                    print("""        _________________
        |               |         
        |               O
        |             
        |            
        |             
        |                      
        |
        |                      """)
                    print("".join(word_mistery))
                elif count_of_mistakes == 2:
                    print("""        _______________
        |             |         
        |             |
        |             O
        |             |                                      
        |                      
        |
        |                   """)
                    print("".join(word_mistery))
                elif count_of_mistakes == 3:
                    print("""        _______________
        |             |         
        |             |
        |             O
        |             |\                                     
        |                      
        |
        |                   """)
                    print("".join(word_mistery))
                elif count_of_mistakes == 4:
                    print("""        _______________
        |             |         
        |             |
        |             O
        |            /|\                                      
        |                      
        |
        |                   """)
                    print("".join(word_mistery))
                elif count_of_mistakes == 5:
                    print("""        _______________
        |             |         
        |             |
        |             O
        |            /|\                                      
        |            /         
        |
        |                   """)
                    print("".join(word_mistery))
                elif count_of_mistakes == 6:
                    print("""        _______________
        |             |         
        |             |
        |             O
        |            /|\                                      
        |            / \        
        |
        |                   """)
                    continue
                print("У вас осталось {} попыток!".format(6 - count_of_mistakes))
    else:
        print()
        if count_of_mistakes < 6:
            print("Вы выиграли! Молодец!")
        elif count_of_mistakes == 6:
            print("Ох, нет! Вы проиграли!")
            print(f"Загаданное слово - {answer}")


word_list = ["собака", "тетрис", "человек", "лосось", "мужчина",
             "женщина", "работа", "россия", "ребенок", "голова", "вопрос"]

word_answer = random.choice(word_list)
while True:
    choose_the_letter(word_answer)
    flag = replay()
    if flag == 1:
        print("Отлично. Игра не бывает лишней!")
        print()
    elif flag == 0:
        print("Хорошо. До встречи!")
        break