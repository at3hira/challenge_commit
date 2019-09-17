"""
・Create Hexagon object and class
・find the Hexagon perimeter length output result

"""

class Hexagon:
    def __init__(self, one_side):
        """
        Parameters
        -----------
            one_side : int or float
            hexagon one side length
        """
        self.one_side = one_side

    def calculate_perimeter(self):
        """
        return
        -----------
            return : int or float
            Hexagonal perimeter length
        """
        return self.one_side * 6

hexagon = Hexagon(12)
perimeter = hexagon.calculate_perimeter()
print(perimeter)
