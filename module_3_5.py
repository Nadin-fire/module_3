def get_multiplied_digits (number):
    str_number = str(number)
    first = int(str_number [0])
    while str_number.endswith('0'):  # если number оканчивается на '0', убираем его
        str_number = str_number[:len(str_number) - 1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:])) #умножаем первую цифру числа на рез-т работы этой же ф-ции с числом, но уже без первой цифры
    else:
        return first



result = get_multiplied_digits(40203)
result1 = get_multiplied_digits(24220000)
print(result)
print(result1)