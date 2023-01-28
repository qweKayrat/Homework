# print("Задание 1", end="\n\n")
#
# lst = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# print()
# print(f'Список: {lst}')
# new_lst = []
# for i in lst:
#     if i > 0:
#         new_lst.append(i)
# print(f'Новый список, состоящий из положительных элементов: {new_lst}')
# new_lst.sort(reverse=True)
# print(f'Наибольший элемент списка: {new_lst[0]}')
#

# print("Задание 2", end="\n\n")
#
# lst = [int(input("-> ")) for i in range(int(input("n = ")))]
# index_k = int(input("Введите индекс:\nk = "))
# value_c = int(input("Введите значение:\nс = "))
# lst.insert(index_k, value_c)
# print(lst)

# print("Задание 3", end="\n\n")
# lst = [int(input("-> ")) for i in range(int(input("n = ")))]
# number_ch = int(input("Введите число:\nсh = "))
#
# if number_ch in lst:
#     print("Число присутствует в элементах списка")
# else:
#     print("Такого числа нет в элементах списка")
