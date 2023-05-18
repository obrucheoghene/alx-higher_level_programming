#!/usr/bin/python3
""" 101-main """

from os.path import dirname, abspath, join
import sys
current_path = dirname(abspath(__file__))
parent_path = abspath(join(current_path, '..'))
sys.path.append(parent_path)

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)