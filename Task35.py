#Написать программу получающую набор произведений чисел от 1 до N.
def set_multiplication(n):
    result = 1
    for i in range(1,n+1):
        result *= i
        print(result)
n = int(input('Введите число: '))
set_multiplication(n)