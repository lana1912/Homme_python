# 3. По заданному номеру дня недели вывести его название
def Week(n):
    res = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    return res[n-1]
n = int(input('Введите день: '))
print(Week(n))