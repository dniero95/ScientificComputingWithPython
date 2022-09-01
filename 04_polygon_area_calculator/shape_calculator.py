class Rectangle:
    def __init__(self, width, height):
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

    def get_amount_inside(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__width}, {self.__height})'



class Square(Rectangle):
    pass