# Задание 1

dct = {i: i ** 3 for i in range(1, 11)}

print(dct)

# Задание 2

s1 = set(input("Введите первую строку: "))
s2 = set(input("Введите вторую строку: "))

print("Искомыми буквами являются:")
[print(i, end=" ") for i in s1 - s2]
print()

# Задание 3

s3 = set(input("Введите первую строку: "))
s4 = set(input("Введите вторую строку: "))

print("Искомыми буквами являются:")
[print(i, end=" ") for i in s3 | s4]
print()

# Задание 4

s5 = set(input("Введите первую строку: "))
s6 = set(input("Введите вторую строку: "))

print("Искомыми буквами являются:")
[print(i, end=" ") for i in s5 ^ s6]
print()
