#Программа определиния принадлежности точки графику бабочки
#Программа сделанна Динь Вьет Ань группа ИУ7-14Б


while True:
    x, y = map(float, input('Введите координаты: ').split())
    ok = False

    #Верхняя правая часть крыльев
    if (1 <= x <= 9 and y <= (-1/8)*(x-9)**2+8) and ((1 <= x <= 8 and y >= (1/49)*(x-1)**2) or (8 <= x <= 9 and y >= 7*(x-8)**2+1)):
        ok = True

    #Верхняя левая часть крыльев               
    if (-9 <= x <= -1 and y <= (-1/8)*(x+9)**2+8) and ((-9 <= x <= -8 and y >= 7*(x+8)**2+1) or (-8 <= x <= -1 and y >= (1/49)*(x+1)**2)):
        ok = True

    #Нижняя правая часть крыльев                
    if ((2 <= x <= 8 and y >= (1/3)*(x-5)**2-7) or (1 <= x <= 2 and y >= 2*(x-1)**2-2)) and (1 <= x <= 8 and y <= (-4/49)*(x-1)**2):
            ok = True

    #Нижняя левая часть крыльев
    if ((-8 <= x <= -2 and y >= (1/3)*(x+5)**2-7) or (-2 <= x <= -1 and y >= 2*(x+1)**2-2)) and (-1 <= x <= -8 and y <= (-4/49)*(x+1)**2):
            ok = True

    #Туловище
    if -1 <= x <= 1 and y <=-4*x**2+2 and -1 <= x <= 1 and y >= 4*x**2-6:
            ok = True

    #Усы        
    if 0 <= abs(x) <= 2 and (y == (3/2)*x+2 or y == -3/2*x + 2):
        ok = True
            
    if ok: print('Точка принадлежит графике')
    else: print('Точка не принадлежит графике')
    

