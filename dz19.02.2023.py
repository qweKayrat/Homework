# Задание 1

def decorator(func):
    avg = 0

    def wrapper(*args):
        nonlocal avg
        avg = func(*args) / len(args)
        print(f"Среднее арифметическое чисел {str(args).replace('(', '').replace(')', '')} = {avg}")

        # Тут добавил replace(), для того чтобы вывод был без скобок картежа

    return wrapper


@decorator
def summa(*args):
    summ = 0
    for i in args:
        summ += i
    print(f"Сумма чисел {str(args).replace('(', '').replace(')', '')} = {summ}")
    # Тут добавил replace(), для того чтобы вывод был без скобок картежа

    return summ


summa(2, 3, 3, 4)

print("\n" + "-" * 100 + "\n")


# Задание 2

def change_to_str(string, c_old, c_new):  # Разделение между задачами
    string2 = ""

    for i in string:
        if i == c_old:
            i = c_new
        string2 += i
    return string2


str1 = "Я изучаю Nython. Мне нравится Nythot. Nytnot очень интересный язык программирования."
str2 = change_to_str(str1, "N", "P")
print("str1 =", str1)
print("str2 =", str2)

print("\n" + "-" * 100 + "\n")  # Разделение между задачами


# Задание 3

def del_character_by_position(string, pos):
    string = string[:pos] + string[pos + 1:]
    return string


s = "0123456789"
s2 = del_character_by_position(s, 4)
print("s =", s)
print("s2 =", s2)

print("\n" + "-" * 100 + "\n")  # Разделение между задачами


# Задание 4

def del_full_character(string, del_character):
    str_new = ""
    for i in string:
        if i == str(del_character):
            str_new += ""
            continue
        str_new += i
    return str_new


s = '012345363738494'
s2 = del_full_character(s, 3)
print(s)
print(s2)
