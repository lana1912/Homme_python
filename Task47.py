# 47.Строка содержит набор чисел. Показать большее и меньшее число
""" A = input('Введите числа: ').split
for i in range(len(A)): A[i] = int(A[i])
print(A)
print(f'Большее число', max(A))
print(f'Наименьшее число', min(A)) """

A = input('Введите числа  ').split() 
#for i in range(len(A)): A[i] = int(A[i]) 
A = [int(i) for i in A]
print('Полученный список', A) 
print(f'Большее число', max(A)) 
print(f'Меньшее число',min(A))