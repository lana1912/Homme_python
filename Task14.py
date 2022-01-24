import re


14.# Найти третью цифру числа или сообщить, что её нет
def third_digit(n):
    result = 0
    if n % 100 < 1 :
        result = n % 100 / 10
        result = int(result)
    else:
        return 'Третьей цифры нет'
    return result
print(third_digit(14))
