# 44.В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов
lst = [1.1, 1.2, 3.1, 5, 10.01] 
lst = list(map(lambda e: e % 1, lst,))
print(max(lst) - min(lst))
print(lst)