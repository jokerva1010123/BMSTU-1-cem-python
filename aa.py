# Программа сделана Динь Вьет Ань, ИУ7-14Б
# Определить длины сторон треугольника по заданным целочисленным координатам вершин
# Определить является ли треугольник равнобедренным
# Найти медиану, проведенную из наименьшего угла треугольника
# Ввести координаты одной точки и определить находиться ли внутри треугольника
# Если да, найти расстояние от нее до ближайшей стороны

from math import sqrt, fabs

xa, ya = map(int, input('Введите координаты вершины А: ').split())
xb, yb = map(int, input('Введите координаты вершины B: ').split())
xc, yc = map(int, input('Введите координаты вершины C: ').split())

AB = sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))        # Вычисляет длину АВ
AC = sqrt((xa-xc)*(xa-xc) + (ya-yc)*(ya-yc))        # Вычисляет длину АС
BC = sqrt((xc-xb)*(xc-xb) + (yc-yb)*(yc-yb))        # Вычисляет длину ВС
if fabs(AB - AC + BC) <= 10**-8 or fabs(AB + AC - BC) <= 10**-8 or fabs(BC + AC - AB) <= 10**-8:
    print('Это не треугольник')
else:
    print('Длина стороны АB: {:g}'.format(AB))
    print('Длина стороны АC: {:g}'.format(AC))
    print('Длина стороны BC: {:g}'.format(BC))

    # Треугольник с двумя равными сторонами - это равнобедренный треугольник
    if fabs(AB - AC) <= 10**-8 or fabs(AB - BC) <= 10**-8 or fabs(AC - BC) <= 10**-8:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник не равнобедренный')

    # Медиана из А: АМ = sqrt((2*(AB*AB+AC*AC) - BC*BC)/4)
    median = 0
    if AB <= AC and AB <= BC:
        median = sqrt((2*(AC*AC+BC*BC) - AB*AB)/4)      # Угол С наименьший, то вычисляет медиану из С
    elif AC <= AB and AC <= BC:
        median = sqrt((2*(AB*AB+BC*BC) - AC*AC)/4)      # Угол В наименьший, то вычисляет медиану из B
    elif BC <= AB and BC <= AC:
        median = sqrt((2*(AB*AB+AC*AC) - BC*BC)/4)      # Угол А наименьший, то вычисляет медиану из A
    print('Медиана из наименьшего угла треугольника: {:g}'.format(median))

    xd, yd = map(float, input('Введите одной точки D: ').split())
    s = 1/2 * abs((xc-xa)*(yb-ya) - (yc-ya)*(xb-xa))        # Вычисляет площадь треугольник ABC
    s1 = 1/2*abs((xd-xa)*(yb-ya)-(yd -ya)*(xb-xa))          # Вычисляет площадь треугольник ABD
    s2 = 1/2*abs((xd-xc)*(yb-yc)-(yd-yc)*(xb-xc))           # Вычисляет площадь треугольник BCD
    s3 = 1/2*abs((xd-xa)*(yc-ya)-(yd-ya)*(xc-xa))           # Вычисляет площадь треугольник ACD
    # Если сумма площадей треугольников равна площади основного треугольника, то точка лежит внутри, иначе - снаружи.
    if fabs(s - s1 - s2 - s3) > 10**-8:
        print('Точка не находится внутри треугольника')
    else:
        print('Точка находится внутри треугольника')
        DAB = 2*s1 / AB                  # Вычисляет расстояние от точки до АВ
        DBC = 2*s2 / BC                  # Вычисляет расстояние от точки до ВС
        DAC = 2*s3 / AC                  # Вычисляет расстояние от точки до АС
        print('Расстояние от точки до ближайшей стороны: {:g}'.format(min(min(DAB, DAC), DAB)))