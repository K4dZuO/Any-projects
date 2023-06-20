def info():
    text = input("""Введите текст, который требуется зашифровать: 
""")
    print()
    first_key = list(
        map(str, input("Введите первый ключ и количество операций через пробел в формате 'кей 250': ").split()))
    key1 = first_key[0].lower()
    iter1 = int(first_key[1])

    second_key = list(map(str, input("Введите второй ключ и количество операций через пробел: ").split()))
    key2 = second_key[0].lower()
    iter2 = int(second_key[1])

    third_key = list(map(str, input("Введите третий ключ и количество операций через пробел: ").split()))
    key3 = third_key[0].lower()
    iter3 = int(third_key[1])

    fourth_key = list(map(str, input("Введите четвертый ключ и количество операций через пробел: ").split()))
    key4 = fourth_key[0].lower()
    iter4 = int(fourth_key[1])

    return [text, key1, iter1, key2, iter2, key3, iter3, key4, iter4]


def encode(text, key, iter):
    upper_rus_alphabet = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    lower_rus_alphabet = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    key_digits = [lower_rus_alphabet.index(x) for x in list(key)] # индексы афлавите без ё
    for i in range(iter):
        new_text = ""
        index_key = 0
        for symbol in text:
            if symbol not in " .,!?:1234567890":
                if symbol in upper_rus_alphabet:
                    new_text += upper_rus_alphabet[(upper_rus_alphabet.index(symbol) + key_digits[index_key])%32]
                    index_key += 1
                    index_key %= len(key_digits)
                elif symbol in lower_rus_alphabet:
                    new_text += lower_rus_alphabet[(lower_rus_alphabet.index(symbol) + key_digits[index_key]) % 32]
                    index_key += 1
                    index_key %= len(key_digits)
            else:
                new_text += symbol
        text = new_text
    print()
    print(f"""Текст после шифрования ключом "{key}" {iter} раз:
{text}""")
    return text


def decode(text, key, iter):
    upper_rus_alphabet = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    lower_rus_alphabet = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    key_digits = [lower_rus_alphabet.index(x) for x in list(key)] # индексы афлавите без ё
    for i in range(iter):
        new_text = ""
        index_key = 0
        for symbol in text:
            if symbol not in " .,!?:1234567890":
                if symbol in upper_rus_alphabet:
                    new_text += upper_rus_alphabet[(upper_rus_alphabet.index(symbol) - key_digits[index_key])%32]
                    index_key += 1
                    index_key %= len(key_digits)
                elif symbol in lower_rus_alphabet:
                    new_text += lower_rus_alphabet[(lower_rus_alphabet.index(symbol) - key_digits[index_key]) % 32]
                    index_key += 1
                    index_key %= len(key_digits)
            else:
                new_text += symbol
        text = new_text
    print()
    print(f"""Текст после дешифрования ключом "{key}" {iter} раз:
{text}""")
    return text


def Vige_code(information):
    print()
    print("-" * 100 + "   ШИФРОВАНИЕ   " + "-" * 100)
    text, key1, iter1, key2, iter2, key3, iter3, key4, iter4 = information[0], information[1], information[2], \
    information[3], information[4], information[5], information[6], information[7], information[8]
    text = encode(text, key1, iter1) # шифрование
    text = encode(text, key2, iter2)
    text = encode(text, key3, iter3)
    text = encode(text, key4, iter4)

    print("-"*100 + "   ДЕШИФРОВАНИЕ   "+"-"*100)

    text = decode(text, key4, iter4)
    text = decode(text, key3, iter3)
    text = decode(text, key2, iter2)
    text = decode(text, key1, iter1)


information = info()
Vige_code(information)
