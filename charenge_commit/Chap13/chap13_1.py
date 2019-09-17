
class Rectangle:
    def __init__(self, w, l):
        """
            Parameters
            ----------
            w : int
                Rectangular width
            l : int
                Rectangular length
        """
        self.width = w
        self.length = l
    
    def calculate_perimeter(self):
        """ Calculation of the perimeter of the rectangle
            Return
            ------
            Rectangular perimeter
        """
        return self.width * 2 + self.length * 2

class Square:
    def __init__(self, one_side):
        """
            Parameters
            ----------
            one_side : int
                Length of one side
        """
        self.one_side = one_side
    
    def calculate_perimeter(self):
        """ Calculation of the perimeter of the Square
            Return
            ------
            Square perimeter
        """
        return self.one_side * 4


rectangle = Rectangle(5, 9) # Create rectangle object
area_rectangle = rectangle.calculate_perimeter() # Call calculate_perimeter method of the Rectangle class
print(area_rectangle)

square = Square(12) # Create square object
area_square = square.calculate_perimeter() # Call calculate_perimeter method of the Square class
print(area_square)