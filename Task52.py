# 52. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

lst = [4, 5, 6, 8, 8, 10]
result = list(set(lst))

""" result = [] 
for i in lst:
    count = 0
    for j in result:
        if i == j:
            count += 1
    if count == 0:
        result.append(i)"""
print(result)
