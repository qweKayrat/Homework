# Задание 1
tpl1 = ('ab', 'abcd', 'cde', 'abc', 'def')


def search_element(tpl, el):
    if el in tpl:
        print("Yes")
    else:
        print("No")


s = input('Введите поисковый элемент "s" : ')
search_element(tpl1, s)

# Задание 2

s = int(input('Введите по порядку, без пробелов, элементы кортежа: '))


def int_to_tuple(digits):
    tpl = ()
    while digits:
        num = digits % 10
        tpl += (num,)
        digits //= 10
    return tpl[::-1]


def stat_tuple(digits):
    tpl = int_to_tuple(digits)
    print(tpl)
    for i in range(10):
        if i in tpl:
            print(f'Количество {i} = {tpl.count(i)}')
        else:
            continue


stat_tuple(s)
