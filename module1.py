
a = 1
b = 1
if a == b:
    raise ValueError('равны')
print("круто")

# Нахождение площади через другие углы
cos_angle2 = (self.side1.__len__() ** 2 + self.side2.__len__() ** 2 - self.side3.__len__() ** 2) / 2 / self.side1.__len__() / self.side2.__len__()
sin_angle2 = sqrt(1 - cos_angle2 ** 2)
area2 = 0.5 * self.side1.__len__() * self.side2.__len__() * sin_angle2
cos_angle3 = (self.side2.__len__() ** 2 + self.side3.__len__() ** 2 - self.side1.__len__() ** 2) / 2 / self.side2.__len__() / self.side3.__len__()
sin_angle3 = sqrt(1 - cos_angle3 ** 2)
area3 = 0.5 * self.side2.__len__() * self.side3.__len__() * sin_angle3
print(area1, area2, area3)


list_side = [side1, side2, side3]
max = list_side[index]
index_max = 0
for index_1 in range(1, 3):
    if list_side[index] > max:
        max = list_side[index]
        index_max = index_1
else:
    list_side.remove(index_max)

    for index_2 in range(3):
        if index_1 == index_2:
            continue


        def area(self):
        if self.convex():
            trangle1 = Triangle(self.side1, self.side2, self.diagonal1)
            trangle2 = Triangle(self.diagonal1, self.side3, self.side4)
            return trangle1.area() +  trangle2.area()

        a = Point(0, 0)
b = Point(3, 6)
c = Point(4, 4)
d = Point(6, 4)
abcd_3 = Quadrangle(a, b, c, d)
print(abcd_3)
print(abcd_3.convex())