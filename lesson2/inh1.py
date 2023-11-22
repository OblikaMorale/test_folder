class Table:
    def __init__(self, length, width, heigth):
        self.length = length
        self.width = width
        self.heigth = heigth

class Desk(Table):
    def area(self):
        return self.length*self.width
    