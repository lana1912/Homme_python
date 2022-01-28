#11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
import random
def first_digit(n):
    result1 = 0
    result1 = n // 10
    return result1
def second_digit(n):
    result2 = 0
    result2 = n % 10
    return result2
def maximum(n):
    max = first_digit(n)
    if first_digit(n) < second_digit(n):
        max = second_digit(n)
    return max
n = random.randint(10,99)
print('Случаное число из отрезка: ')
print(n)
first_digit(n)
second_digit(n)
print('Максимальная цифра:')
print(maximum(n)) 
























