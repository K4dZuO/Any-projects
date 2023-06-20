def choose_base():
    print("Напишите основание системы счисления вашего числа (от 2 до 16): ", end="")
    old_base = int(input())
    print("Напишите новое основание системы счисления (от 2 до 16): ", end="")
    new_base = int(input())
    return old_base, new_base


def is_valid(old_base):
    if old_base < 11:
        valid_digits = [str(x) for x in range(old_base)]
    elif old_base == 11:
        valid_digits = [str(x) for x in range(10)] + [chr(65 + i) for i in range(old_base - 10)]
    elif old_base == 12:
        valid_digits = [str(x) for x in range(10)] + [chr(65 + i) for i in range(old_base - 10)]
    elif old_base == 13:
        valid_digits = [str(x) for x in range(10)] + [chr(65 + i) for i in range(old_base - 10)]
    elif old_base == 14:
        valid_digits = [str(x) for x in range(10)] + [chr(65 + i) for i in range(old_base - 10)]
    elif old_base == 15:
        valid_digits = [str(x) for x in range(10)] + [chr(65 + i) for i in range(old_base - 10)]
    elif old_base == 16:
        valid_digits = [str(x) for x in range(10)] + [chr(65 + i) for i in range(old_base - 10)]
    print(valid_digits)
    print("Введите свое число: ", end="")
    flag = False
    while flag == False:
        flag = True
        number = input()
        for digit in number:
            if digit not in valid_digits:
                print(f"Число не принадлежит основанию {old_base}. Проверьте число")
                flag = False
    return number


def transfer_to_10(number):
    sum = 0
    digits_of_10 = [x for x in range(10)]
    for i in range(len(number)):
        symbol = number[-i - 1]
        if symbol.isdigit():
            value_symbol = int(symbol)
        elif symbol == "A":
            value_symbol = 10
        elif symbol == "B":
            value_symbol = 11
        elif symbol == "C":
            value_symbol = 12
        elif symbol == "D":
            value_symbol = 13
        elif symbol == "E":
            value_symbol = 14
        elif symbol == "F":
            value_symbol = 15
        result = value_symbol * old_base ** i
        sum += result
    return sum


def interpritation(number_in_10th, new_base):
    result = ""
    while number_in_10th // new_base != 0:
        remain = number_in_10th % new_base
        if remain in [x for x in range(10)]:
            result = str(remain) + result
        elif remain == 10:
            result = "A" + result
        elif remain == 11:
            result = "B" + result
        elif remain == 12:
            result = "C" + result
        elif remain == 13:
            result = "D" + result
        elif remain == 14:
            result = "E" + result
        elif remain == 15:
            result = "F" + result
        number_in_10th //= new_base
    else:
        remain = number_in_10th
        if remain in [x for x in range(10)]:
            result = str(remain) + result
        elif remain == 10:
            result = "A" + result
        elif remain == 11:
            result = "B" + result
        elif remain == 12:
            result = "C" + result
        elif remain == 13:
            result = "D" + result
        elif remain == 14:
            result = "E" + result
        elif remain == 15:
            result = "F" + result
        return result



old_base, new_base = choose_base()
number = is_valid(old_base)
number_in_10th = transfer_to_10(number)
print(number_in_10th)
result = interpritation(number_in_10th, new_base)
print(f"Число {number} с основанием {old_base} ---> число {result}  с основанием {new_base}")
