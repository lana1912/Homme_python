#20. Ввести номер четверти, показать диапазоны для возможных координат
diapasones = ['(x > 0, y > 0)', '(x < 0, y > 0)', '(x < 0, y < 0)', '(x > 0, y < 0)']
def quarter(q, diapasones):
    return diapasones[q-1]
q = int(input('Введите четверть '))
print(quarter(q, diapasones))