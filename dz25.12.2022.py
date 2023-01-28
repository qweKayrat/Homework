money = int(input("Введите количество копеек от 1 до 99: "))

if 1 <= money <= 99:
    print(money, end=" ")
    if 5 <= money % 10 <= 9 or 10 <= money <= 20:
        print("копеек")
    elif money == 1 or money % 10 == 1:
        print("копейка")
    else:
        print("копейки")
else:
    print("Вы ввели некорректное количество копеек")
