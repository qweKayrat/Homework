# Задание 1
with open('text1.txt', 'w') as create_file1:
    create_file1.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")

pos1 = int(input("Введите номер строки которую необходимо заменить: ")) - 1
pos2 = int(input("Введите номер строки на которую необходимо заменить строку: ")) - 1


def replace_lines(file, line1, line2):
    with open(file, 'r+') as f:
        read_file = f.readlines()
        if -1 < pos1 < len(read_file) and -1 < pos2 < len(read_file):
            read_file[line1], read_file[line2] = read_file[line2], read_file[line1]
            f.seek(0)
            f.writelines(read_file)
        else:
            print("Вы допустили ошибку!!!")
            if pos1 < 0 or pos1 > len(read_file) - 1:
                print(f'\tВы ввели не корректную строку на которую происходит изменение строки. {pos2 + 1} строки нет в файле!')
            if pos2 < 0 or pos2 > len(read_file) - 1:
                print(f'\tВы ввели не корректную заменяемую строку. {pos1 + 1} строки нет в файле!')


replace_lines(create_file1.name, pos1, pos2)

print("\n" + "-" * 100 + "\n")
# Задание 2
with open('text2.txt', 'w') as create_file2:
    create_file2.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")


def reverse_line(file):
    with open(file, 'r+') as f:
        read_file = f.readlines()
        read_file.reverse()
        f.seek(0)
        f.writelines(read_file)


reverse_line(create_file2.name)

print("\n" + "-" * 100 + "\n")
# Задание 3
with open('text2.txt', 'w') as create_file3:
    create_file3.write("первая строка\nстрока номер два\nтретья строка\n4 строка\n")


def counter_words_in_list(lst):
    for i in lst:
        symbol = len(i)
        word = len(i.split())
        print(i, end="")
        print(f' {symbol} симв. {word} сл.')


def counter_file_lines(file):
    with open(file, 'r') as f:
        read_file = f.readlines()
    counter_words_in_list(read_file)
    print(len(read_file), "стр.")


counter_file_lines(create_file3.name)
