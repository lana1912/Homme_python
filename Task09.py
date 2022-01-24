#9. Показать последнюю цифру трёхзначного числа
def Last_Digit(n):
    result = 0
    if n / 100 < 1:
        return 'Ввели не трехзначное число'
    else:
        result = n % 10
    return result
print(Last_Digit(112))