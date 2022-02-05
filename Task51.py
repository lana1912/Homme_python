# 51. Составить список простых множителей натурального числа N
import math

list = []


def prime_factors(num):
    while num % 2 == 0:

        list.append(2)
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):

        while num % i == 0:
            list.append(i)
            num = num / i
    if num > 2:
        list.append(num)


prime_factors(num=int(input('Введите число ')))
print(list)
