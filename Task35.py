#Написать программу получающую набор произведений чисел от 1 до N.
def set_multiplication(n):
    result = 1
    lst = []
    for i in range(1,n+1):
        result *= i
        lst.append(result)
    return lst
n = int(input('Введите число: '))
print(set_multiplication(n))