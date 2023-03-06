names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]


def non_recursive_counter(lst):
    count = 0
    for i in lst:
        if isinstance(i, str):
            count += 1
        else:
            for j in i:
                if isinstance(j, str):
                    count += 1
                else:
                    count += len(j)
    return count


# попытка "кривым" стэком
def stack_counter(lst):
    count = 0
    stack = lst.copy()
    while len(stack) > 0:
        node = stack.pop()
        if isinstance(node, str):
            count += 1
        else:
            for i in node:
                if isinstance(i, list):
                    count += len(i)
                else:
                    count += 1
    return count


print(non_recursive_counter(names))
print(stack_counter(names))
