# 36.Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму
def sum_elements(n):
    summ = [((1 + (1 / i)) * i) for i in range (1, n+1)]
    print(summ)
    return sum(summ)
n = int(input('Введите число: '))
print(sum_elements(n))
