#33 Пользователь задаёт две строки. Определить количество вхождений одной строки в другую.
def occurrences(text, text2):
     index = text.count(text2)
     return index
text = str(input('Введите первую строку: '))
text2 = str(input('Введите вторую строку: '))
print(occurrences(text, text2))

