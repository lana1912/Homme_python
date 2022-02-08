# 46.Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
def fibonacci(n):
    if n in [0, 1]:
        return 1
    if n > 0:
        return fibonacci(n-1) + fibonacci(n-2)
    if n < 0:
        return fibonacci(n+2) - fibonacci(n+1)


a = int(input('Введите число: '))
list_fibo = [fibonacci(i) for i in range(-a-1, a)]
print(list_fibo)
