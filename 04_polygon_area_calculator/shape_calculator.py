

class Rectangle:
    def __init__(self, width:int, height:int):
        self.__width = width
        self.__height = height

    def set_width(self, width):
        self.__width =  width

    def  set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2* (self.__width + self.__height)

    def get_diagonal(self):
        return (self.__width ** 2 + self.__height ** 2) ** .5

    def get_picture(self):
        if self.__height > 50 or self.__width > 50:
            return f'Too big for picture.'

        picture = f''
        for i in range(self.__height):
            for j in range(self.__width):
                picture = f'{picture}*'
            picture = f'{picture}\n'

        return picture

    def get_amount_inside(self, shape:object):
        return self.get_area() // shape.get_area()

    def __repr__(self):
        return f'{self.__class__.__name__}(width={self.__width}, height={self.__height})'



class Square(Rectangle):

    def __init__(self, side:int):
        super().__init__(side, side)
        self.__side = side
    def set_side(self,side:int):
        self.__side = side
        super().set_height(side)
        super().set_width(side)

    def set_width(self, side):
        self.set_side(side)

    def  set_height(self, side):
        self.set_side(side)

    def __repr__(self):
        return f'{self.__class__.__name__}(side={self.__side})'










