# Вариант Площадь - глобальная переменная
s = 0


def square_parallelepiped1(a, b, c):
    global s

    def square_rectangle1(i, j):
        return i * j

    ab, ac, bc = square_rectangle1(a, b), square_rectangle1(a, c), square_rectangle1(b, c)
    s = 2 * (ab + ac + bc)


square_parallelepiped1(2, 4, 6)
print(s)
square_parallelepiped1(5, 8, 2)
print(s)
square_parallelepiped1(1, 6, 8)
print(s)

print('-' * 8)


# Вариант Площадь - локальная переменная
def square_parallelepiped2(a, b, c):
    def square_rectangle1(i, j):
        return i * j

    ab, ac, bc = square_rectangle1(a, b), square_rectangle1(a, c), square_rectangle1(b, c)

    s1 = 2 * (ab + ac + bc)
    return s1


s2 = square_parallelepiped2(2, 4, 6)
print(s2)
s2 = square_parallelepiped2(5, 8, 2)
print(s2)
s2 = square_parallelepiped2(1, 6, 8)
print(s2)

print('-' * 8)


# Вариант Площадь - не локальная переменная


def square_parallelepiped3(a, b, c):
    s3 = 0

    def square_rectangle3(i, j):
        nonlocal s3
        s3 += i * j

    square_rectangle3(a, b)
    square_rectangle3(a, c)
    square_rectangle3(b, c)
    return 2 * s3


print(square_parallelepiped3(2, 4, 6))
print(square_parallelepiped3(5, 8, 2))
print(square_parallelepiped3(1, 6, 8))
