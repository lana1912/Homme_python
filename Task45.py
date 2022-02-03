# 45. Написать программу преобразования десятичного числа в двоичное
a = int(input())
result = []

while a:
    result.append(a % 2)
    a //= 2
result.reverse()
print(result)
