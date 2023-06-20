def choose_lenguage():
    print("Скажите, какой язык выбрать? Скажите 'ru' или 'en'")
    while True:
        ans_len = input()
        if ans_len == "ru":
            return ans_len
        elif ans_len == "en":
            return ans_len
        else:
            print("Язык не определен. Повторите.")


def encode_or_decode():
    print("Что нужно сделать: закодировать или декодировать сообщение? Скажите 'encode' или 'decode'")
    while True:
        ans_code = input()
        if ans_code == "encode":
            return ans_code
        elif ans_code == "decode":
            return ans_code
        else:
            print("Действие не определено. Повторите.")


def shift_change(ans_len):
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    while True:
        if ans_len == "ru":
            print("Введите значение сдвига от 1 до 32")
            while True:
                shift = int(input())
                if 1 <= shift <= 32:
                    return shift, upper_rus_alphabet, lower_rus_alphabet
                else:
                    print("Некорретное значение сдвига. Повторите")
                continue
        elif ans_len == "en":
            print("Введите значение сдвига от 1 до 25")
            while True:
                shift = int(input())
                if 1 <= shift <= 25:
                    return shift, upper_eng_alphabet, lower_eng_alphabet
                else:
                    print("Некорретное значение сдвига. Повторите")
                continue


def ceasar(shift, code, upper_alphabet, lower_alphabet):
    print("Введи свое сообщение")
    text = input()
    result = ""
    n = len(upper_alphabet)
    for symbol in text:
        if symbol not in " .+-!?,()1234567890":
            if symbol == symbol.upper():
                index_up = upper_alphabet.index(symbol)
                if code == "encode":
                    result += upper_alphabet[(index_up + shift) % n]
                elif code == "decode":
                    result += upper_alphabet[(index_up - shift) % n]
            elif symbol == symbol.lower():
                index_low = lower_alphabet.index(symbol)
                if code == "encode":
                    result += lower_alphabet[(index_low + shift) % n]
                elif code == "decode":
                    result += lower_alphabet[(index_low - shift) % n]
        else:
            result += symbol


    return result

lenguage = choose_lenguage()
code = encode_or_decode()
shift, up_alpabet, low_alphabet = shift_change(lenguage)
print(ceasar(shift, code, up_alpabet, low_alphabet))
