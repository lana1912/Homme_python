#Посчитать сумму цифр в вещественном числе
def sum_numbers(n):
    text = str(n)
    result = 0
    for i in range(0, len(text)):
        if text[i] != '.':
            result += int(text[i])
    return result
n = float(input('Введите вещественное число: '))
print(sum_numbers(n))