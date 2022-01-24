#18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
for x in range(0,2):
    for y in range(0,2):
        print(not(x or y) == (not x and not y))

