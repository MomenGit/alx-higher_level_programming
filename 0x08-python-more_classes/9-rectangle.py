#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle object class

    Args:
        width (int): The width of the rectangle
            (defaults to 0) must be greater than or equal to 0
        height (int): The height of the rectangle
            (defaults to 0) must be greater than or equal to 0

    Attributes:
        number_of_instances (int): The number of rectangle instances
        print_symbol (str): The symbol of string
            representation of the rectangle
            (defaults to '#')
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width: int = 0, height: int = 0) -> None:
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def area(self):
        """Calculate the rectangle instance's area

        Returns:
            Rectangle instance's area, given by height * width
        """

        return self.height * self.width

    def perimeter(self):
        """Calculate the rectangle instance's perimeter

        Returns:
            Rectangle instance's perimeter, given by 2 * (height + width)
        """

        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.height + self.width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""

        return cls(size, size)

    def __str__(self) -> str:
        """Returns an informal and nicely printable string representation
           of the rectangle instance, using print_symbol attribute.
           (Returns an empty string on height=0 or width=0)
        """

        rectangle = ''
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            rectangle = rectangle + \
                str(type(self).print_symbol)*self.width+"\n"
        return rectangle.removesuffix('\n')

    def __repr__(self) -> str:
        """Returns a string representation of the rectangle
           to be able to recreate a new instance by using eval()
        """

        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
