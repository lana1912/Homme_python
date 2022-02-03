# 42. Найти сумму чисел списка стоящих на нечетной позиции.
from random import randint


lst = [randint(-15, 15) for i in range(6)]
print(lst)
result = sum(lst[1::2])
print(result)
