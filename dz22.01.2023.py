from random import randint

print("Задание 1", end="\n\n")

lst1 = [randint(0, 100) for i in range(20)]
print(lst1)
res = sum(lst1)
print(f'Сумма списка = {res}')

print("\nЗадание 2", end="\n\n")

lst2 = [[randint(0, 10) for j in range(6)] for g in range(6)]
for row1 in lst2:
    for x in row1:
        print(x, end="\t\t")
    print()

lst3 = [randint(0, 10) for y in range(6)]
print("\n", lst3, end="\n\n", sep="")
for row2 in lst2:
    ind = lst2.index(row2)
    if ind % 2 == 0:
        lst2.remove(row2)
        lst2.insert(ind, lst3)
    for x in range(len(row2)):
        print(lst2[ind][x], end="\t\t")
    print()
