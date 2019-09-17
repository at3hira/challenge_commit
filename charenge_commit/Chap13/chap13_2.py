

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

    def change_size(self, change_date):
        """ Change the value of the square object
            Parameters
            ----------
            change_date : int
        """
        self.one_side += change_date


rectangle = Rectangle(5, 9) # Create rectangle object
area_rectangle = rectangle.calculate_perimeter() # Call calculate_perimeter method of the Rectangle class
print(area_rectangle)

square.change_size(20)
area_square_two = square.calculate_perimeter()
print(area_square_two)