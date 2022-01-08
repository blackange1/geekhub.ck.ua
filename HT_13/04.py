"""
Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор
 фігури при створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.
"""
from math import pi


class Figure(object):
    def __init__(self, color='white') -> None:
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class Square(Figure):
    def __init__(self, width=1, height=1, color='white') -> None:
        super().__init__(color=color)
        self.width = width
        self.height = height

    def get_square(self) -> float:
        return self.width * self.height
    
    def get_perimeter(self) -> float:
        return (self.width + self.height) * 2


class Oval(Figure):
    def __init__(self, r=1, R=1, color='white') -> None:
        super().__init__(color=color)
        self.r = r
        self.R = R

    def get_square(self) -> float:
        return self.R * self.r * pi
