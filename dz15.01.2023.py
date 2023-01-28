print('Задание 1 "Угадай число"', end="\n\n")
import random
computer = random.randint(1, 100)
n = 1

while True:
    person = int(input("Введите число от 1 до 100 "))
    if person == 0:
        print("Зря вы сдались =(, загаданное число было: ", computer)
        break
    elif person > computer:
        print("Загаданное число меньше")
    elif person < computer:
        print("Загаданное число больше")
    else:
        # person == computer:
        print("Вы угадали загаданное число c", n, "раза")
        break
    n += 1

print('\nЗадание 2 "Четные индексы"', end="\n\n")
n = [input("->") for i in range(int(input("n = ")))]

for i in range(len(n)):
    if i % 2 == 0:
        print(n[i], end=" ")

print('\nЗадание 3 "Больше предыдущего"', end="\n\n")
n = [input("->") for i in range(int(input("n = ")))]
for i in range(len(n)):
    if n[i] > n[i-1]:
        print(n[i], end=" ")

# 4 Немного не догадался как это сделать с тем что мы прошли, сделал через подсчёт повторений
print('\nЗадание 4 "Одно вхождение"')
lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for i in range(len(lst)):
    r = 0
    for j in range(len(lst)):
        if i == j:
            continue
        elif lst[i] == lst[j]:
            r = 1
        else:
            continue
    if r == 0:
        print(lst[i], end=" ")
