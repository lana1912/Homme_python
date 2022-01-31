# 40.Определить, присутствует ли в заданном списке строк, некоторое число 
text = ['len', '24', 'apple', 'work', '36']
def certain_number(n):
    lst = str(n)
    return lst in text
print(certain_number(24))