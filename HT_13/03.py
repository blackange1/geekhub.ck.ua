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
    def __init__(self, width=1, height=1) -> None:
        self.width = width
        self.height = height

    def get_square(self) -> float:
        return self.width * self.height
    
    def get_perimeter(self) -> float:
        return (self.width + self.height) * 2


class Oval(Figure):
    def __init__(self, r=1, R=1) -> None:
        self.r = r
        self.R = R

    def get_square(self) -> float:
        return self.R * self.r * pi


tmp = Square()
tmp.set_color('red')
print(Square.color)