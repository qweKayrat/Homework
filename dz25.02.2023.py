# Задание 1

def text_in_brackets(string):
    text = string[string.find("(") + 1:string.find(")")]
    return text


s = "Дана ст(рока символов, среди которых есть одна открыв)ающаяся"
print(text_in_brackets(s))

print("\n" + "-" * 100 + "\n")


# Задание 2

def replace_string(string, old_s, new_s):
    return string.replace(old_s, new_s)


s = input("Строка: ")
old_sub = input("Ее заменяемая подстрока: ")
new_sub = input("Новая подстрока: ")
s = replace_string(s, old_sub, new_sub)
print(s)

print("\n" + "-" * 100 + "\n")


# Задание 3

def count_e_in_text(txt):
    txt1 = len([e for e in txt.strip().replace("\n", " ").split(" ") if e[0].lower() == 'е'])
    return txt1


text = """Ежевику для ежат
Принесли два ежа
Ежевику еле-еле
Ежата возле ели съели.
"""

print("Количество слов:", count_e_in_text(text))
