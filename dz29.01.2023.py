# Задание 1
from math import pi

figure = 0
while True:
    figure = int(input("Выберите фигуру: \n1-Прямоугольник 2-треугольник 3-круг: "))
    if figure < 1 or figure > 3:
        print("Вы ввели некорректный номер фигуры =(")
    else:
        break
h = float(input("Введите длины высоты: "))
w = float(input("Введите длину основания: "))


def area_figure(a, height, width):
    match a:
        case 1:
            return height * width
        case 2:
            return (height * width) / 2
        case 3:
            return (w ** 2 * pi) / 4


print(round(area_figure(figure, h, w), 2))

# Задание 2
lst_exmp = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
simple = []

for i in range(2, 100):
    for j in simple:
        if i % j == 0:
            break
    else:
        simple.append(i)


def min_list(lst):
    min_lst = []
    for x in lst_exmp:
        if x in simple:
            min_lst.append(x)
    return min(min_lst)


def max_list(lst):
    max_lst = []
    for x in lst_exmp:
        if x not in simple:
            max_lst.append(x)
    return max(max_lst)


print(f'Min: {min_list(lst_exmp)}\nMax: {max_list(lst_exmp)} ')
