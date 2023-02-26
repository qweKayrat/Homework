import re


# Задание 1

def validate_password(psw):
    reg = r'[A-Za-z0-9@_-]{6,18}'
    if re.findall(reg, psw) == [psw]:
        return True
    else:
        return False


password = 'my-p@ssword'
print(validate_password(password))

print("\n" + "-" * 100 + "\n")


# Задание 2

def search_mail(mail):
    reg = r'[\w.-]+@\D?[.\w]+'
    return re.findall(reg, mail)


test = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
print(search_mail(test))
