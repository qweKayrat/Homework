num = 43235
a = num % 10
num //= 10
b = num % 10
num //= 10
c = num % 10
num //= 10
d = num % 10
num //= 10
e = num % 10
sumInt = a + b + c + d + e
resInt = a * b * c * d * e
avgInt = sumInt / 5
print("Произведение: " + str(resInt) + "\nСреднее арифметическое: " + str(avgInt))
