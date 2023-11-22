import random

class List_numbers(list):

    __list_size = 0

    def __init__(self, list_size = 1):
        self.__list_size = list_size
        x = 1
        if self.__list_size < 100 :
            while x <= self.__list_size:
                self.append(0)
                x += 1
        else:
            print('Список не должен быть больше 100 элементов!')
        x = 0

    def input_data(self, index, data):
        if self.__list_size > index and index >= 0:
            self.insert(index, data)
        elif index < 0:
            print('Индекс не должен быть меньше 0!')
        else:
            print('Индекс выходит за пределы списка! - '+str(self.__list_size))
    
    def fill_random(self):
        x = 0
        while x < self.__list_size:
            self[x] = random.randint(0, 100)
            x += 1
        x = 0

    def find(self, element):
        if isinstance(element, int):
            l = list()
            x = 0
            while x < self.__list_size:
                if self[x] == element:
                    l.append(x)
                x += 1
            x = 0
            
            if len(l) > 0:
                print(l)
            else:
                print('Указанного элемента нет в списке!')
        else:
            print('Элемент должен быть INT!')
        
    def remove(self, element):
        if isinstance(element, int):
            x = 0
            while x < self.__list_size:
                if self[x] == element:
                    self[x] = 0
                x += 1
            x = 0
        else:
            print('Элемент должен быть INT!')

    def max(self):
        x = 0
        res = 0
        while x < self.__list_size:
            if res < self[x]:
               res = self[x]
            x += 1
        x = 0
        return res
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            x = 0
            min_len = 0
            if len(self) < len(other):
                min_len = len(self)
            else:
                min_len = len(other)
            
            while x < min_len:
                self[x] = self[x] + other[x]
                x += 1
            x = 0
        else:
            print(f"Объект {other.__name} должен быть типа - List_numbers!")