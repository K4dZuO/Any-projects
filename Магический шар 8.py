import random

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

def get_answer():
    print("Привет Мир! Я - магический шар, и я знаю ответ на любой твой вопрос.")
    print("Скажи-ка мне, как твое имя?")
    user_name = input()
    print(f"""А, так ты у нас {user_name}. Ну что же, тогда давай я отвечу на все твои вопросы. 
Что бы ты хотела узнать?""")
    while True:
        question = input()
        print(random.choice(answers))
        print("""Таков мой ответ. Если хочешь задать еще один вопрос, то скажи 'еще'.
        Если ты узнала все, что хотела, то скажи 'стоп'.""")
        result = input()
        while True:
            if result == "еще":
                print("Еще не все? Тогда быстрее задавай новый вопрос!")
                break
            elif result == "стоп":
                return print("Увидимся позже :)")
            else:
                print("Не уверен, что понял тебя")


get_answer()