#31 Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.
def many(N):
    numbers = {1}
    temp = 1
    for i in range(1,N):
        temp *= -3
        numbers.add(temp)
    return numbers
print(many(6))