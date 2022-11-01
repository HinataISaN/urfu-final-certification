
from math import sqrt

class Point:
    def __init__(self, x, y):
        if (type(x) in [int, float]) and (type(y) in [int, float]) or x == None and y == None:
            self.x = x
            self.y = y
        else:
            raise ValueError('Coordinates of Point is type int or float')

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
class Segment:
    def __init__(self, point_a, point_b):
        if not (isinstance(point_a, Point) and isinstance(point_b, Point)):
            raise ValueError('Coordinates of Segment is type Point')
        if point_a == point_b:
            raise ValueError('Отрезок состоит из двух разных точек')
        self.start = point_a
        self.end = point_b

    def __repr__(self):
        return 'Segment(start -> {}, end -> {})'.format(self.start, self.end)

    def __len__(self):
        return sqrt((self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2)

    def __lt__(self, other):
        return self.__len__() < other.__len__()

    def __le__(self, other):
        return self.__len__() <= other.__len__()

    def compare_of_lentgh(self, other):         # Функция сравнения длины отрезков на равенство
        return self.__len__() == other.__len__()

    def __eq__(self, other):                    # Функция, сравнивающая совпадение отрезков по координатам
        if self.start == other.start and self.end == other.end or self.start == other.end and self.end == other.start:
            return True
        else:
            return False

    # Функция, которая определяет знак двух векторных произведений на оси oz для вектора, 
    # делящего пространство на две полуплоскости и векторов проведенных от конца, делящего отрезка, до двух концов другого отрезка
    def sign_vector_product(self, other):                        # Здесь векторное произведение всегда имеет только одну компоненту, т.к. векторы рассматриваются на плоскости OXY
        vector_self = Point(self.end.x - self.start.x, self.end.y - self.start.y)       # Здесь координаты вектора задаются тоже через класс Point
        vector_to_start_other = Point(other.start.x - self.start.x, other.start.y - self.start.y)
        vector_to_end_other = Point(other.end.x - self.start.x, other.end.y - self.start.y)
        vectprod_to_start_other = vector_self.x * vector_to_start_other.y - vector_self.y * vector_to_start_other.x    # Координата z векторного произведения отрезков с плоскости OXY
        vectprod_to_end_other = vector_self.x * vector_to_end_other.y - vector_self.y * vector_to_end_other.x
        if vectprod_to_start_other * vectprod_to_end_other <= 0:
            return True
        else:
            return False

    def intersection(self, other):     # Функция, определяющая пересекаются ли отрезки
        check_1 = self.sign_vector_product(other)
        check_2 = other.sign_vector_product(self)
        if check_1 == check_2 == True:
            return True     # Отрезки пересекаются
        else:
            return False    # Отрезки НЕ пересекаются

class Triangle:
    def __init__(self, element_1, element_2, element_3):
        sides_or_points = [element_1, element_2, element_3]              
        list_number_points_sides = Triangle.check_points_or_sides(sides_or_points)
        if list_number_points_sides[1] == 3:        # list_number_points_sides[1] - количество отрезков среди полученного списка sides_or_points
            points = self.check_create_triangle_with_sides(sides_or_points)
            if points:
                self.point1 = points[0]
                self.point2 = points[1]
                self.point3 = points[2]
                self.side1 = element_1
                self.side2 = element_2
                self.side3 = element_3
            else:
                raise ValueError('Из отрезков с данными координатами невозможно создать треугольник')
        elif list_number_points_sides[0] == 3:      # list_number_points_sides[0] - количество точек среди полученного списка sides_or_points
            if element_1 == element_2 or element_1 == element_3 or element_2 == element_3:
                raise ValueError('Из данных точек невозможно создать треугольник')
            else:
                self.point1 = element_1
                self.point2 = element_2
                self.point3 = element_3
                self.side1 = Segment(element_1, element_2)
                self.side2 = Segment(element_2, element_3)
                self.side3 = Segment(element_3, element_1)
        else: 
                raise TypeError('Expected three points (class Point) or three sides (class Segment)')

    def check_points_or_sides(list_sides_or_points):    # Функция для подсчета среди пришедших в класс аргументов количества точек и отрезков
        list_number_points_sides = [0, 0]           # Здесь нулевой элемент - количество объектов класса точка в присланном списке, первый элемент - количество объектов класса отрезок в присланном списке 
        for element in list_sides_or_points:
            if isinstance(element, Point):
                list_number_points_sides[0] += 1
            elif isinstance(element, Segment):
                list_number_points_sides[1] += 1 
        return list_number_points_sides

    def search_unique_points(list_sides, num_angeles):  # Функция для определения количества неповторяющихся точек на концах переданных в класс отрезков
        list_points = []
        for side in list_sides:
            list_points.append(side.start)
            list_points.append(side.end)
        for index in range(2 * num_angeles):       # Выуживаем с помощью циклов и ифов количество неповторяющихся точек среди концов данных отрезков
            if list_points[index] == Point(None, None):
                continue
            for index_check in range(2 * num_angeles):
                if index == index_check:
                    continue
                if list_points[index] == list_points[index_check]:
                    list_points[index] = Point(None, None)
                    break
        list_points_new = []                
        for point in list_points:                  # Записываем в новый список только не повторяющиеся точки концов отрезков
            if point == Point(None, None):
                continue
            list_points_new.append(point)
        if len(list_points_new) == num_angeles:
            return list_points_new
        else:
            return False

    def check_create_triangle_with_sides(self, list_sides):     # Функция, определяющая возможность построения треугольника из переданных в класс отрезков
        if list_sides[0] == list_sides[1] or list_sides[1] == list_sides[2] or list_sides[0] == list_sides[2]:
            raise ValueError('Из отрезков с данными координатами невозможно создать треугольник')
        return Triangle.search_unique_points(list_sides, 3)
           
    def __repr__(self):
        return 'Triangle: {}\n          {}\n          {}\n'.format(self.side1, self.side2, self.side3)

    def perimeter(self):
        return self.side1.__len__() + self.side2.__len__() + self.side3.__len__()
    # Функция, возвращающая характеристику об одном из углов рассматриваемого треугольника
    # углов в треугольнике три, соответственно передаем номер угла в аргументе функции и получаем ответ - острый он, тупой или прямой 
    def angle(self, number_angle=1):    
        if number_angle == 1:
            check = self.side1.__len__() ** 2 + self.side3.__len__() ** 2 - self.side2.__len__() ** 2
        elif number_angle == 2:
            check = self.side1.__len__() ** 2 + self.side2.__len__() ** 2 - self.side3.__len__() ** 2
        elif number_angle == 3:
            check = self.side2.__len__() ** 2 + self.side3.__len__() ** 2 - self.side1.__len__() ** 2
        else:
            raise ValueError('There is three angles in triangle. Choose one from three (1, 2 or 3)')

        def what_is_angle(check):
            if check > 0:
                return 'острый'
            elif check < 0:
                return 'тупой'
            else:
                return 'прямой'

        if number_angle == 1:
            return 'Угол треугольника, соответсвующий вершине в точке {} - {}'.format(self.point1, what_is_angle(check))
        elif number_angle == 2:
            return 'Угол треугольника, соответсвующий вершине в точке {} - {}'.format(self.point2, what_is_angle(check))
        else:
            return 'Угол треугольника, соответсвующий вершине в точке {} - {}'.format(self.point3, what_is_angle(check))

    def area(self):
        cos_angle1 = (self.side1.__len__() ** 2 + self.side3.__len__() ** 2 - self.side2.__len__() ** 2) / 2 / self.side1.__len__() / self.side3.__len__() 
        sin_angle1 = sqrt(1 - cos_angle1 ** 2)
        return 0.5 * self.side1.__len__() * self.side3.__len__() * sin_angle1

    # Функция, возвращающая отрезок - медиану от номера переданного в аргументе угла треугольника
    # до противоположной стороны 
    def median(self, number_angle=1):   
        
        def calculation_median(point, side):
            middle_point_x = (side.start.x + side.end.x) / 2
            middle_point_y = (side.start.y + side.end.y) / 2
            middle_point = Point(middle_point_x, middle_point_y)
            return Segment(point, middle_point)

        if number_angle == 1:
            return calculation_median(self.point1, self.side2)
        elif number_angle == 2:
            return calculation_median(self.point2, self.side3)
        elif number_angle == 3:
            return calculation_median(self.point3, self.side1)
        else:
            raise ValueError('There is three angles in triangle. Choose one from three (1, 2 or 3)')
   
class Quadrangle:
    def __init__(self, element_1, element_2, element_3, element_4):
        sides_or_points = [element_1, element_2, element_3, element_4]
        list_number_points_sides = Triangle.check_points_or_sides(sides_or_points)
        if list_number_points_sides[0] == 4:      # list_number_points_sides[0] - количество точек среди полученного списка sides_or_points
            if element_1 == element_2 or element_1 == element_3 or element_1 == element_4 or element_2 == element_3 or element_2 == element_4 or element_3 == element_4:
                raise ValueError('Из данных точек невозможно создать четырехугольник')
            else:
                self.point1 = element_1
                self.point2 = element_2
                self.point3 = element_3
                self.point4 = element_3
                self.side1 = Segment(element_1, element_2)
                self.side2 = Segment(element_2, element_3)
                self.side3 = Segment(element_3, element_4)
                self.side4 = Segment(element_4, element_1)
                self.diagonal1 = Segment(element_1, element_3)
                self.diagonal2 = Segment(element_2, element_4)
        elif list_number_points_sides[1] == 4:        # list_number_points_sides[1] - количество отрезков среди полученного списка sides_or_points
            points = self.check_create_fourangle_with_sides(sides_or_points)
            if points:
                self.point1 = points[0]
                self.point2 = points[1]
                self.point3 = points[2]
                self.point3 = points[3]
                self.side1 = element_1
                self.side2 = element_2
                self.side3 = element_3
                self.side4 = element_4
                self.diagonal1 = Segment(points[0], points[2])
                self.diagonal2 = Segment(points[1], points[3])
            else:
                raise ValueError('Из отрезков с данными координатами невозможно создать четырехугольник')
        else:
            raise TypeError('Expected four points (class Point) or four sides (class Segment)')
        
    # Функция, проверяющая возможность создания четырехугольника из переданных в класс отрезков
    def check_create_fourangle_with_sides(self, list_sides):
        if list_sides[0] == list_sides[1] or list_sides[0] == list_sides[2] or list_sides[0] == list_sides[3] or list_sides[1] == list_sides[2] or list_sides[1] == list_sides[3] or list_sides[2] == list_sides[3]:
            raise ValueError('Из отрезков с данными координатами невозможно создать треугольник')
        return Triangle.search_unique_points(list_sides, 4)

    def __repr__(self):
        return 'Fourangle: {}\n           {}\n           {}\n           {}'.format(self.side1, self.side2, self.side3, self.side4)

    def perimeter(self):
        return self.side1.__len__() + self.side2.__len__() + self.side3.__len__() + self.side4.__len__()

    def convex(self):
        if self.diagonal1.intersection(self.diagonal2):
            return True         # Четырехугольник выпуклый
        else:
            return False        # Четырехугольник  НЕ выпуклый'

    def area(self):
        if self.convex():
            trangle1 = Triangle(self.side1, self.side2, self.diagonal1)
            trangle2 = Triangle(self.diagonal1, self.side3, self.side4)
            return trangle1.area() + trangle2.area()
        else:
            if self.diagonal1.sign_vector_product(self.diagonal2):
                trangle1 = Triangle(self.side1, self.side2, self.diagonal1)
                trangle2 = Triangle(self.diagonal1, self.side3, self.side4)                
            else:
                trangle1 = Triangle(self.side4, self.side1, self.diagonal2)
                trangle2 = Triangle(self.diagonal2, self.side2, self.side3)
            return trangle1.area() + trangle2.area()

# Проверка инициализации объекта точка
#print(Point(0, 0))
#print(Point(0, 1.5))
#print(Point('0', 0))       # Проверка исключения

# Проверка инициализации объекта отрезок
#a = Point(0, 0)
#с = Point(3, 4)
#ac = Segment(a, с)
#print(ac)
#print(Segment(ac, a))      # Проверка исключения
#print(Segment('c', a))     # Проверка исключения

# Проверка операции сравнения отрезков по длине
#a = Point(0, 0)
#b = Point(3, 4)
#c = Point(-3, -4)
#ac = Segment(a, c)
#ab = Segment(a, b)
#cb = Segment(c, b)
#print('a = {}'.format(a), 'b = {}'.format(b), 'c = {}'.format(c), sep='\n')
#print('ac < ab -> ', ac < ab)
#print('ac < cb -> ', ac < cb)
#print('cb > ab -> ', cb > ab)
#print('ac > ab -> ', ac > ab)
#print('|ac| = |ab| -> ', ac.compare_of_lentgh(ab))
#print('|ab| = |cb| -> ', ab.compare_of_lentgh(cb))
#print('ac <= ab -> ', ac <= ab)
#print('ac <= cb -> ', ac <= cb)
#print('cb <= ac -> ', cb <= ac)
#print('ac >= ab -> ', ac >= ab)
#print('cb >= ac -> ', cb >= ac)
#print('ac >= cb -> ', ac >= cb)

# Проверка существования точек пересечения у двух отрезков
#a = Point(1, 3)
#b = Point(4, 5)
#c = Point(1, 5)
#d = Point(3, 3)

#ab = Segment(a, b)
#cd = Segment(c, d)
#print(ab.intersection(cd))     # Пересекающиеся отрезки

#o = Point(0, 0)
#k = Point(1, 0)
#ok = Segment(o, k)
#print(ok.intersection(ab))      # Непересекающиеся отрезки

#l = Point(2, 4)
#s = Point(4, 4)
#ls = Segment(l, s)
#print(cd.intersection(ls))     # Отрезок соприкасающийся с другим одним из концов


print()

# Проверка на то, что из заданных отрезков или точек может получиться треугольник
#a = Point(1, 3)
#b = Point(4, 5)
#c = Point(1, 5)
#ab = Segment(a, b)
#bc = Segment(b, c)
#ac = Segment(a, c)
#o = Point(0, 0)
#k = Point(1, 0)
#ok = Segment(o, k)
#print(Triangle(ac, bc, ab))
#print(Triangle(a, b, c))
#print(Triangle(ab, ab, bc))    # Проверка исключения
#print(Triangle(a, a, b))       # Проверка исключения
#print(Triangle(ab, bc, ok))    # Проверка исключения
#print(Triangle(ab, bc, a))     # Проверка исключения
#print(Triangle(ab, 'ac', bc))  # Проверка исключения

# Проверка того, какой в треугольнике угол острый тупой или прямой
#triangle_1 = Triangle(Point(4, 0), Point(0, 3), Point(0, 0))
#print(triangle_1.angle(1))
#print(triangle_1.angle(2))
#print(triangle_1.angle(3))
#triangle_2 = Triangle(Point(-3, 1), Point(0, 0), Point(1, -3))
#print(triangle_2.angle(1))
#print(triangle_2.angle(2))
#print(triangle_2.angle(3))
#print(triangle_2.angle(4))      # Проверка исключения

# Проверка рассчета площади
#triangle_1 = Triangle(Point(4, 0), Point(0, 3), Point(0, 0))
#triangle_2 = Triangle(Point(-3, 1), Point(0, 0), Point(1, -3))
#print(triangle_1.area())
#print(triangle_2.area())

# Проверка функции для нахождения медианы
#triangle_1 = Triangle(Point(4, 0), Point(0, 3), Point(0, 0))
#print(triangle_1.median(1))
#print(triangle_1.median(2))
#print(triangle_1.median(3))
#triangle_2 = Triangle(Point(-3, 1), Point(0, 0), Point(1, -3))
#print(triangle_2.median(1))
#print(triangle_2.median(2))
#print(triangle_2.median(3))
#print(triangle_2.median(4))         # Проверка исключения

# Проверка на то, что из заданных отрезков или точек может получиться четырехугольник
#a = Point(1, 3)
#b = Point(1, 5)
#c = Point(4, 5)
#d = Point(3, 3)
#abcd_1 = Quadrangle(a, b, c, d)
#print(abcd_1)
#print(abcd_1.area())              # ответ - 5

#print(abcd_1.convex())           # Проверка выпуклости - выпуклый
#print(abcd_1.perimeter())       # Проверка функции вычисления периметра ответ - 9,23...
#ab = Segment(a, b)
#bc = Segment(b, c)
#cd = Segment(c, d)
#da = Segment(d, a)
#abcd_2 = Quadrangle(ab, bc, cd, da)
#print(abcd_2)

#o = Point(0, 0)
#k = Point(1, 0)
#ok = Segment(o, k)
#print(fourangle_1 = Quadrangle(ab, bc, cd, ok))         # Проверка исключения
#print(fourangle_1 = Quadrangle(ab, bc, cd, cd))         # Проверка исключения
#print(fourangle_1 = Quadrangle(a, b, d, d))             # Проверка исключения
#print(fourangle_1 = Quadrangle(ab, bc, cd, 'ok'))       # Проверка исключения

#a = Point(0, 0)
#b = Point(3, 6)
#c = Point(4, 4)
#d = Point(6, 4)
#abcd_3 = Quadrangle(a, b, c, d)
#print(abcd_3)
#print(abcd_3.convex())      # невыпуклый
#print(abcd_3.area())        # рассчет площади невыпуклого четырехугольника ответ - 10

#ac = Segment(Point(1, 2), Point(3, 2))
#bd = Segment(Point(4, 4), Point(4, 1))
#print(ac.intersection(bd))

