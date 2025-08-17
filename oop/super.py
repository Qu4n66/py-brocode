
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self): #method over writting
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")
        

class Circle(Shape):
    def __init__(self, color, filled, radius ):
        super().__init__(color, filled) #ke thua attribute tu class cha
        self.radius = radius
    
    def describe(self):#method over writting
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")
        super().describe() #ke thua method tu class cha


class Square(Shape):
    def __init__(self, color, filled, width ):
        super().__init__(color, filled)
        self.width = width


class Triangle(Shape):
    def __init__(self, color, filled, width, height ):
        super().__init__(color, filled)
        self.width = width
        self.height = height


circle = Circle(color = 'Red',filled = True,radius = 5)
square = Square(color = 'blue',filled = False,width=3 )
triangle = Triangle(color = 'green',filled = True,width= 4, height = 5)


circle.describe()

square.describe()
