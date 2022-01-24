#19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
result = ''
def quarter(x, y):
    if(x>0) and (y>0): result = '1 четверть'
    if(x<0) and (y>0): result = '2 четверть'
    if(x<0) and (y<0): result = '3 четверть'
    if(x>0) and (y<0): result = '4 четверть'
    return result
print(quarter(1.2,-3.4))