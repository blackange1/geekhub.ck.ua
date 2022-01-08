"""
Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням 
white і метод для зміни кольору фігури,
а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ 
для завдання початкових розмірів об'єктів при їх створенні.
"""
from math import pi


class Figure(object):
    color = "white"

    @classmethod
    def set_color(cls, color) -> None:
        cls.color = color


class Square(Figure):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def get_square(self) -> float:
        return self.width * self.height
    
    def get_perimeter(self) -> float:
        return (self.width + self.height) * 2


class Oval(Figure):
    def __init__(self, r1, r2) -> None:
        self.r1 = r1
        self.r2 = r2

    def get_square(self) -> float:
        return self.r1 * self.r2 * pi


tmp = Square(2, 2)
tmp.set_color('red')
print(Square.color)