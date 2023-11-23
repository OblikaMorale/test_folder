from abc import ABC, abstractmethod
from enum import Enum, unique
from dataclasses import dataclass

@unique
class FuelType(Enum):
    disel = 0
    gasoline = 1

@dataclass
class Engine:
    name: str
    type: FuelType
    k: float = 1

class Vehicle(ABC):
    classname = None

    @abstractmethod
    def __init__(self, name = ''):
        self.name = name
        self._speed = 0
        self._fuel = 0
        self._engine = 1
        self._engine_type = Engine('v6',FuelType.gasoline,2)
        self._tank = 50
        self._max_speed = 100
        self._capacity = 0 
        self._max_capacity = 20 


    @property #getter
    def capacity(self):
        return self._capacity
    
    @capacity.setter #setter - загрузка
    def capacity(self, value):
        if value > self._max_capacity:
            self._capacity = self._max_capacity
        else:
            self._capacity = value if value > 0 else 0


    @property #getter
    def fuel(self):
        return self._fuel
    
    @fuel.setter #setter - заправка
    def fuel(self, value):
        if value + self._fuel > self._tank:
            self._fuel = self._tank
        else:
            self._fuel = value if value > 0 else 0
    
    @property #getter
    def speed(self):
        return self._speed
    
    @speed.setter #setter
    def speed(self, value):
        if value > self._max_speed:
            self._speed = self._max_speed
        else:
            self._speed = value if value > 0 else 0

    def __str__(self):
        return f'{self.name}: объем двигателя - {self._engine}, топливо - {self._fuel}, скорость - {self._speed}'

    def __repr__(self):
        return str(self)
    
    def gas_exp(self):
        if self._max_capacity > 0 and self._max_speed > 0:
            print(f'Расход топлива - {float((self._engine_type.k+self._capacity/self._max_capacity+self._speed/self._max_speed))*self._engine} л/100км')
        else:
            print(f'Не корректны входные параметры: Макс. скорость - {self._max_speed}, Макс. грузоподъемность - {self._max_capacity}')

    def trip_time(self, path_value = 0):
        r = 1
        t = 1

        r = float((self._engine_type.k+self._capacity/self._max_capacity+self._speed/self._max_speed))*self._engine

        if self._fuel <= 0: raise ValueError(f'Пустой бак, залейте, пожалуйста, горючее!')
        if self._speed <= 0: raise ValueError(f'{self.classname} стоит, задайте, пожалуйста, скорость движения!')
        
        if r > 0:
            t = self._fuel/r
            if path_value > 0 and path_value < self._speed * t:
                t = path_value/self._speed
                print(f'При уровне топлива - {self._fuel} и скорости - {self._speed} расстояние - {path_value} будет пройдено за {t}')
            else:
                print(f'При уровне топлива - {self._fuel} и скорости - {self._speed} время пути - {t}')
        
    

class Car(Vehicle):
    classname = 'Автомобиль'

    def __init__(self, name):
        super().__init__(name)
        self._engine = 2
        self._tank = 80
        self._max_speed = 200 
        self._capacity = 0 
        self._max_capacity = 4
        self._engine_type = Engine('v4',FuelType.gasoline,2)

    def gas_exp(self):
        super().gas_exp()

class Track(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self._engine = 7
        self._tank = 120
        self._max_speed = 100    
        self._capacity = 20
        self._capacity = 0 
        self._max_capacity = 20
        self._engine_type = Engine('v8',FuelType.disel,4)

    def gas_exp(self):
        super().gas_exp(self)


class Bus(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self._engine = 5
        self._tank = 100
        self._max_speed = 120
        self._capacity = 40 
        self._capacity = 0 
        self._max_capacity = 40 
        self._engine_type = Engine('v4',FuelType.gasoline,3)  

    def gas_exp(self):
        super().gas_exp(self)  

