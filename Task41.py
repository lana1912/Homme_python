# 41.Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
lst = ['homme', 'today', 'cat', 'homme']


def find(text):
    result = 0
    for i in range(0, len(lst)):
        if text == lst[i]:
            result += 1
            if result == 2:
                return i
    if result < 2:
        return 'Второго вхождения нет'


print(find(text=str(input('Введите строку:  '))))
