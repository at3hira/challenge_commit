import math
"""
・create Circle Object
・find the area of circle, output result
"""

class Circle:
    def __init__(self, r):
        """
        Parameters
        ----------
            r : int
            circle radius
        """
        self.radius = r
    
    def area(self):
        """
        Returns
        ----------
            return : float
            circle area
        """
        return self.radius ** 2 * math.pi

circle = Circle(5)
circle_area = circle.area()
print(circle_area)