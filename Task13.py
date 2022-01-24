#13. Выяснить, кратно ли число заданному, если нет, вывести остаток.
result = 0
def multiplicity(a , b):
    if a % b != 0:
        result = a % b
    else:
        result = 'Кратно'
    return result 
b = int(input('Введите число: '))
print(multiplicity(10,b))