# 37.Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

data = []
with open("File37.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])
pos1 = data[0]
pos2 = data[1]
print(pos1, pos2)
def elements(lst):
    N = 5
    for i in range(-N,N+1):
        lst.append(i)
    return lst 
def multu(lst):
    return pos2 == lst [10]
lst = []
print(elements(lst))
print(multu(lst))