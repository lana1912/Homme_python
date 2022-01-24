#21. Программа проверяет пятизначное число на палиндромом.
def palindrome(n):
    text = str(n)
    if n / 100000 > 1 or n / 10000 < 1 :
        return 'Введите другое число'
    else:
        text = str(n)
        return text[0]==text[4] and text[1]==text[3]
print(palindrome(25652))
