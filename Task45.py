# 45. Написать программу преобразования десятичного числа в двоичное
a = int(input())
result = ' '

while a:
    result = str(a % 2) + result
    a //= 2

print(result)
