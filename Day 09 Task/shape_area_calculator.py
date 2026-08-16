class Circle:
    def area(self):
        r = 5
        print("Circle Area =", 3.14 * r * r)


class Rectangle:
    def area(self):
        l = 10
        w = 5
        print("Rectangle Area =", l * w)


class Triangle:
    def area(self):
        b = 6
        h = 8
        print("Triangle Area =", 0.5 * b * h)


shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.area()