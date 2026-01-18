def input_int(message):
    is_correct_input = False
    number = 0

    while is_correct_input == False:
        try:
            number = int(input(f"{message}"))
            is_correct_input = True
        except:
            print("Ошибка. Вы ввели НЕ число")

    return number


def get_sum(a, b):
    result = a + b
    return result


def print_result(result):
    print(f"сумма = {result}")


a = input_int("введите первое число: ")
b = input_int("введите второе число: ")

result = get_sum(a, b)

print_result(result)
