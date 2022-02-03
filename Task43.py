# 43.Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint


lst = [randint(0, 15) for i in range(6)]
print(lst)
if len(lst) % 2 != 0:  # проверка на разную длину списка
    count = 1
else:
    count = 0
print([lst[i] * lst[len(lst) - i - 1]
      for i in range(0, len(lst) // 2 + count)])
