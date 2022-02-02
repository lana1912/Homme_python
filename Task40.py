# 40.Определить, присутствует ли в заданном списке строк, некоторое число 
text = ['len', '24', 'apple', 'work', '36']
text = list(filter(lambda e:'36' in e , text))
print(text)
