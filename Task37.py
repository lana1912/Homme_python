# 37.Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

from fileinput import close
from random import randint

N = int(input('Введите число: '))
lst = [randint(-N,N+1) for i in range(15)]
print(lst)
with open('File37.txt', 'r') as F:
    pos = [int(x) for x in F]
F.close()
print(pos)
result = 1
for i in range(0,len(lst)):
    for j in range(0, len(pos)):
        if pos[j] == i:
            result *= lst[i]
print(result)
