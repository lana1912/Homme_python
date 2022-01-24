#15. Дано число. Проверить кратно ли оно 7 и 23
def multiplicity(n):
    return n % 7 ==0 and n % 23 ==0
print(multiplicity(161))