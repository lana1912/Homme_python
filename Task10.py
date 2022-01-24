#10. Показать вторую цифру трёхзначного числа
result = 0
def second_digit(n):
    if n / 100 < 1:
        return 'Число не трехзначное'
    else:
       result = n % 100 / 10
       result = int(result)
    return result
print(second_digit(146))