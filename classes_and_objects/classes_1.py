class Hello_class:
    name_1 = 1
    name_2 = 2

    def test_func1(self):
        return 25
    

class car:
    car_count = 0
    def __init__(self, name = 'default_car', make = 'default_make', year = 2000):
        self.name = name
        self.make = make
        self.year = year
        self.__class__.car_count += 1

    def start(self):
        print('Engine start')

    def stop(self):
        print('Engine stop')

tesla = car()
tesla.start()