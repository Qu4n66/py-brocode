
#property: add additional logic when read,write, or delete atrributes
# Getter: read
# setter: write
# deleter: delete



class Retangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height # getter
    
    @property # setter
    def width(self):
        return f'{self._width:.1f} cm'
    @property
    def height(self):
        return f'{self._height:.1f} cm'
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else: print('Width must be greater than zero')

    @height.setter # use to check if new data is allow else, it keep the previous one
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else: print('height must be greater than zero')

    @width.deleter
    def width(self):
        del self._width
        print('Width has been deleted')
    @height.deleter
    def width(self):
        del self._height
        print('height has been deleted')

rectangle = Retangle(3,4)


rectangle.width = 4
rectangle.height = 6

del rectangle.width
del rectangle.height

        



