import random


def generaty_password(chars, length):
    result_list = random.sample(chars, length)
    result = "".join(result_list)
    return result

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
ambiguity = "il1Lo0O"
chars = ""


print("Сколько паролей создать?")
count_of_passwords = int(input())

print("Сколько символов должен содержать один пароль?")
lenght_of_password = int(input())

print("Пароль должен содержать цифры? Скажите 'y' или 'n'")
answer = input()
if answer == "y":
    chars += digits

print("Пароль должен содержать прописные буквы? Скажите 'y' или 'n'")
answer = input()
if answer == "y":
    chars += uppercase_letters

print("Пароль должен содержать строчные буквы? Скажите 'y' или 'n'")
answer = input()
if answer == "y":
    chars += lowercase_letters

print("Пароль должен содержать символы '!#$%&*+-=?@^_'? Скажите 'y' или 'n'")
answer = input()
if answer == "y":
    chars += punctuation

print("Исключать ли неоднозначные символы 'il1Lo0O'? Скажите 'y' или 'n'")
answer = input()
if answer == "y":
    for symbol in ambiguity:
        chars = chars.replace(symbol, "")


for _ in range(count_of_passwords):
    print(generaty_password(chars, lenght_of_password))
