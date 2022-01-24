# 4. Найти максимальное из трех чисел
def Maximum(a,b,c):
    max = a
    if b > a and b > c:
        max = b
    if c > a and c > b:
        max = c
    return max
print('Максимальное число: ')
print(Maximum(4, 6, 8))