class Rectangle:

    __length = 0
    __width = 0

    def __init__(self, length = 0, width = 0):
        self.__length = length
        self.__width = width

    def __str__(self):
        return f"Длина - {self.__length} Ширина - {self.__width}."
    
    def __repr__(self):
        return str(self)
    
    def perimetr(self):
        return self.__length*2+self.__width*2
    
    def area(self):
        return self.__length*self.__width
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.area() == other.area()
        else:
            return False
        

a = Rectangle(3,4)