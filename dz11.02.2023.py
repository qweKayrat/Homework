# Задание 1

lst_key = ['red', 'green', 'blue']
lst_value = ['#FF0000', '#008000', '#0000FF']
dct = {k: v for k, v in zip(lst_key, lst_value)}
print(dct)

# Задание 2

dct1 = {1: 10, 2: 20}
dct2 = {3: 30, 4: 40}
dct3 = {5: 50, 6: 60}
dct1.update(dct2 | dct3)
print(dct1)
# если нужно было объединить словари в другой новый словарь
dct4 = dct1 | dct2 | dct3
print(dct4)

# Задание 3

emp1 = {'name': 'John', 'salary': 7500}
emp2 = {'name': 'Emma', 'salary': 8000}
emp3 = {'name': 'Brad', 'salary': 6500}

# Преобразования в employees сделал только для красивого вывода
employees = dict()
employees['emp1'] = {k: v for k, v in emp1.items()}
employees['emp2'] = {k: v for k, v in emp2.items()}
employees['emp3'] = {k: v for k, v in emp3.items()}

for k, v in employees.items():
    print(k)
    for i in v:
        print("\t", i, ":", employees[k][i])


select_emp = input("\nВведите имя работника: ")
new_salary = int(input("Введите изменение зарплаты работника: "))

if select_emp in emp1.values():
    emp1['salary'] = new_salary
    employees['emp1'].update(emp1)
elif select_emp in emp2.values():
    emp2['salary'] = new_salary
    employees['emp2'].update(emp2)
elif select_emp in emp3.values():
    emp3['salary'] = new_salary
    employees['emp3'].update(emp3)
else:
    print("Вы ошиблись именем работника\n")

for k, v in employees.items():
    print(k)
    for i in v:
        print("\t", i, ":", employees[k][i])
