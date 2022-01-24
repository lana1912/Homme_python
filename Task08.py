# 8. Показать четные числа от 1 до N
def Even(N):
    for i in range(1,N+1):
        if i % 2 == 0:
            print(i)
Even(6)