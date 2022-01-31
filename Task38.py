#38.Реализовать алгоритм перемешивания списка. 
from random import randint 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
count = len(lst) 
while count >= 0:
    count1 = randint(0, len(lst)-1)
    temp = lst[count1]
    lst.pop(count1)
    lst.append(temp)
    count -= 1
print(lst)