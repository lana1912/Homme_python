#12. Удалить вторую цифру трёхзначного числа
def deleting(n):
    list = str(n)
    list = list[0] + list[2]
    return list
print(deleting(245))    