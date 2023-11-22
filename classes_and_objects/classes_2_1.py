import math

class Point:
    __x = 0
    __y = 0
    __color_value = 'none'

    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def set_color(self, color_value = 'Black'):
        self.__color_value = color_value

    def __str__(self):
        return f"Координаты x - {self.__x}, y - {self.__y}, цвет - {self.__color_value}"
    
    def __repr__(self):
        return str(self)
    
class Circle(Point):
    __x = 0
    __y = 0
    __rd = 0
    __color_value = 'none'

    def __init__(self, x, y, rd = 1):
        super().__init__(x, y)
        self.__rd = rd

    def set_color(self, color_value = 'Black'):
        self.__color_value = color_value

    def __str__(self):
        return f"Координаты центра x - {self.__x}, y - {self.__y}, радиус - {self.__rd} цвет - {self.__color_value}"
    
    def __repr__(self):
        return str(self)
    
    def set_radius(self, rd = 1):
        self.__rd = rd

    def area(self):
        return math.pi * self.__rd ** 2
    

class Sphere(Circle):
    __x = 0
    __y = 0
    __rd = 0
    __color_value = 'none'

    def __init__(self, x, y, rd):
        super().__init__(x, y, rd)

    def volume(self):
        return math.pi * self.__rd ** 2
    
    def area(self):
        return 4 * math.pi * self.__rd ** 2  