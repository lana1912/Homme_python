#11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
result1 = 0
result2 = 0 
def first_digit(n):
    result1 = 0
    if n < 10 or n > 99:
        return 'введите другое число'
    else:
       result1 = n % 100 / 10
       result1= int(result1)
    return result1
def second_digit(n):
    result2 = 0
    if n < 10 or n > 99:
        return ''
    else:
       result2 = n % 10
    return result2
def maximum(n):
    max = first_digit(n)
    if first_digit(n) < second_digit(n):
        max = second_digit(n)
    return max
n = int(input('Введите число: '))
print(first_digit(n))
print(second_digit(n))
print('Максимальная цифра:')
print(maximum(n))


